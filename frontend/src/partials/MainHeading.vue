<template>
  <h1 class="text-h2 mb-3">
    {{ text }}
  </h1>
</template>

<script>
export default {
    name: 'MainHeading',
    props: {
      text: String
  }
}
</script>