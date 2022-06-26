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
import { MOCKED_MONTH_DOWNLOAD, MOCKED_MONTH_UPLOAD, MOCKED_TIME_STAMP, USAGE_STAMP_API_ENDPOINT } from '@/consts'

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
  },
  methods: {
    async getData() {
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
    async getMockedData() {
      setTimeout(() => {
        this.$store.commit('updateUsageData', {
          currentMonthDownload: MOCKED_MONTH_DOWNLOAD,
          currentMonthUpload: MOCKED_MONTH_UPLOAD,
          currentTimeStamp: MOCKED_TIME_STAMP
        })
        this.$store.commit('switchLoading')
      }, 2500)
    },
  },
  metaInfo: {
    title: 'App',
    titleTemplate: '%s | Data Usage Monitor',
    meta: [
      { name: 'description', content: 'Data Usage Monitor is a simple application to view data from your Huawei router.' }
    ]
  },
};
</script>
