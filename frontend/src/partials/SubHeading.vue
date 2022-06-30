<template>
  <p class="text-subtitle-1 font-weight-regular">
    {{ text }}
  </p>
</template>

<script>
export default {
    name: 'SubHeading',
    props: {
      text: String
  }
}
</script>