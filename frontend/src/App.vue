<template>
  <v-app>
    <TopBar />

    <LeftNav />

    <Main />
  </v-app>
</template>

<script>
import { TopBar, LeftNav, Main } from '@/partials'
import { MOCKED_MONTH_DOWNLOAD, MOCKED_MONTH_UPLOAD, MOCKED_TIME_STAMP } from '@/consts'

export default {
  name: 'App',
  components: {
    TopBar,
    LeftNav,
    Main
  },
  mounted () {
    this.$vuetify.theme.dark = this.$store.state.darkMode
    this.$meta().refresh()
    setTimeout(() => {
      this.$store.commit('updateUsageData', {
        currentMonthDownload: MOCKED_MONTH_DOWNLOAD,
        currentMonthUpload: MOCKED_MONTH_UPLOAD,
        currentTimeStamp: MOCKED_TIME_STAMP
      })
      this.$store.commit('switchLoading')
      }, 2500)
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
