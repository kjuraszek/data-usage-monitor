<template>
  <v-app>
    <TopBar />

    <LeftNav />

    <Main />
  </v-app>
</template>

<script>
import { TopBar, LeftNav, Main } from '@/partials'

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
