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
      app
      class="pt-10"
      mini-variant-width="80"
      mini-variant
      permanent
      clipped
    >
    <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="selectedItem"
          mandatory
          color="primary"
        >
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :to="{path: item.path}"
          >
            <v-list-item-icon class="my-5">
              <v-icon v-text="item.icon" size="48"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

    </v-navigation-drawer>

    <v-main class="grey lighten-3">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
      selectedItem: 0,
      mini: true,
      items: [
        { text: 'Home', icon: 'mdi-home-heart', path: '/' },
        { text: 'Settings', icon: 'mdi-cogs', path: '/settings' },
        { text: 'Help', icon: 'mdi-help-circle-outline', path: '/help' },
        { text: 'Github', icon: 'mdi-github', path: '/not-found' },
        { text: 'Offline', icon: 'mdi-close-circle-outline', path: '/offline' },
      ],
    }),
};
</script>
