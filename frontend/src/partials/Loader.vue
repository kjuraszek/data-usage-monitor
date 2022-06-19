<template>
<div>
  <v-progress-circular
    color="red darken-4"
    indeterminate
    :rotate="35"
    :size="68"
    :width="6"
    :value="65"
  >
    
  </v-progress-circular>
  <p v-if="text" class="text-subtitle-2 font-weight-regular text-center my-2">
    {{ text }}
  </p>
</div>
</template>

<script>
export default {
    name: 'Loader',
    props: {
      text: String
  }
}
</script>