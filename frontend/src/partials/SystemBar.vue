<template>
  <div>
    <v-system-bar
      app
      clipped-left
      color="error"
    >
      <v-icon>mdi-message-alert</v-icon>
      <span>this application is running on mocked data</span>
    </v-system-bar>
  </div>
</template>

<script>
export default {
    name: 'SystemBar',
}
</script>