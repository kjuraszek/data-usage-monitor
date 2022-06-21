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
  mounted() {
    this.$vuetify.theme.dark = this.$store.state.darkMode
  }
};
</script>
