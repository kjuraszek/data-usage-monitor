<template>
  <v-app>
    <SystemBar v-if="useMockedData"/>

    <TopBar />

    <LeftNav />

    <Main />
  </v-app>
</template>

<script>
import { TopBar, LeftNav, Main, SystemBar } from '@/partials'
import { MOCKED_MONTH_DOWNLOAD, MOCKED_MONTH_UPLOAD, MOCKED_TIME_STAMP, USAGE_STAMP_API_ENDPOINT, AUTOREFRESH_INTERVAL } from '@/consts'

export default {
  name: 'App',
  components: {
    TopBar,
    LeftNav,
    Main,
    SystemBar
  },
  computed: {
      useMockedData () {
        return process.env.VUE_APP_USE_MOCKED_VALUES === "true"
      },
      autoRefresh () {
        return this.$store.state.autoRefresh
      },
      loading () {
        return this.$store.state.loading
      }
  },
  data () {
    return {
      interval: null
    }
  },
  mounted () {
    this.$vuetify.theme.dark = this.$store.state.darkMode
    this.$meta().refresh()
    if (this.useMockedData) {
      this.getMockedData()
    } else {
      this.getData()
    }
    if (this.autoRefresh) {
      this.startInterval()
    }
  },
  methods: {
    async getData () {
      try {
        const response = await this.$http.get(
          USAGE_STAMP_API_ENDPOINT,
          {'Content-Type': 'application/json'})
        this.$store.commit('updateUsageData', {
          currentMonthDownload: response.data.current_month_download,
          currentMonthUpload: response.data.current_month_upload,
          currentTimeStamp: response.data.time_stamp
        })
        this.$store.commit('switchLoading')
      } catch (error) {
        this.$store.commit('switchFailed')
        this.$store.commit('switchLoading')
        console.log(error);
      }
    },
    getMockedData () {
      setTimeout(() => {
        this.$store.commit('updateUsageData', {
          currentMonthDownload: MOCKED_MONTH_DOWNLOAD,
          currentMonthUpload: MOCKED_MONTH_UPLOAD,
          currentTimeStamp: MOCKED_TIME_STAMP
        })
        this.$store.commit('switchLoading')
      }, 2500)
    },
    startInterval () {
      this.interval = setInterval(() => {
        if (!this.loading) {
          this.$store.commit('switchLoading')
        }
        if (this.useMockedData) {
          this.getMockedData()
        } else {
          this.getData()
        }
      }, AUTOREFRESH_INTERVAL)
    }
  },
  watch: {
    autoRefresh (newValue) {
        if (newValue === true) {
          this.startInterval()
        } else {
          if (this.interval) {
            clearInterval(this.interval)
            this.interval = null
          }
        }
      }
  },
  metaInfo: {
    title: 'App',
    titleTemplate: '%s | Data Usage Monitor',
    meta: [
      { name: 'description', content: 'Data Usage Monitor is a simple application to view data from your Huawei router.' }
    ]
  },
  beforeDestroy () {
    clearInterval(this.interval)
  }
};
</script>
