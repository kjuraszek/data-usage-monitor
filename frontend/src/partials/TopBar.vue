<template>
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
</template>

<script>
export default {
    name: 'TopBar',
}
</script>