<template>
<div>
  <v-icon
      size="64"
      color="red darken-4"
    >
      mdi-alert-remove
    </v-icon>
  <p v-if="text" class="text-subtitle-2 font-weight-regular text-center my-2">
    {{ text }}
  </p>
</div>
</template>

<script>
export default {
    name: 'Failed',
    props: {
      text: String
  }
}
</script>