<template>
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
</template>

<script>
export default {
    name: 'LeftNav',
    data: () => ({
      selectedItem: 0,
      items: [
        { text: 'Home', icon: 'mdi-home-heart', path: '/' },
        { text: 'Settings', icon: 'mdi-cogs', path: '/settings' },
      ],
    }),
}
</script>