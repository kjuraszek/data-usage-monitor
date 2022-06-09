<template>
  <v-container>
    <v-row class="text-center">

      <v-col class="my-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Home
        </h1>

        <p class="subheading font-weight-regular">
          Welcome to the Data Usage Monitor dashboard. You can see here a basic informations about the data transfer of your network (based on the data harvested from router).
        </p>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-9">
          Current data usage
        </h2>

        <v-row justify="left">
          <v-col
            v-for="n in 4"
            :key="n"
            cols="12"
            sm="6"
            md="3"
          >
            <v-card>
              <v-card-title>Data Usage #{{n}}</v-card-title>
              <v-card-text>
                <v-progress-circular
                  :rotate="270"
                  :size="150"
                  :width="25"
                  :value="52*n % 99"
                  :color="`blue darken-${n}`"
                >
                  
                </v-progress-circular>
              </v-card-text>
            </v-card>
          </v-col>
          
        </v-row>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Home',
  }
</script>
