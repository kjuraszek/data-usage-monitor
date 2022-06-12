<template>
  <v-container>
    <v-row class="text-center">

      <v-col class="my-10">
        <h1 class="display-2 font-weight-bold mb-3">
          Page Not Found
        </h1>
        
        <p class="subheading font-weight-regular">
          Nothing found under this URL - check if URL is correct or return to home.
        </p>
        <v-btn
          depressed
          color="error"
          to="/"
        >
          Go back
        </v-btn>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'NotFound',
  }
</script>
