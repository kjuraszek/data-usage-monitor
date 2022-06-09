<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      clipped-left
    >
      <div class="d-flex align-center">

        <v-img
          alt="Data Usage Monitor"
          contain
          min-width="100"
          src="@/assets/dum-logo-1.png"
          width="300"
        />
      </div>

    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      app
      class="pt-10"
      color="transparent"
      mini-variant
      permanent
      clipped
    >
      <v-avatar
        v-for="n in 5"
        :key="n"
        color="secondary"
        size="20"
        class="d-block text-center mx-auto mb-9"
      ></v-avatar>
    </v-navigation-drawer>

    <v-main>
      <Home/>
    </v-main>
  </v-app>
</template>

<script>
import Home from './components/Home';

export default {
  name: 'App',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
};
</script>
