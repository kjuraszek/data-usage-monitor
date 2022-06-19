<template>
  <v-container>
    <v-row class="text-center">

      <v-col class="mt-10">
        <MainHeading
          :text="mainTitle"
        ></MainHeading>

        <SubHeading
          :text="subTitle"
        ></SubHeading>

      </v-col>

    </v-row>

    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-card>
          <v-card-title>Appearance</v-card-title>
          <v-card-text>
            <v-switch
                  v-model="$vuetify.theme.dark"
                  label="Dark theme"
                ></v-switch>
          </v-card-text>
          
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import { MainHeading, SubHeading } from '@/partials'

  export default {
    name: "Settings",
    data: () => ({
      mainTitle: "Settings",
      subTitle: "Basic application settings",
    }),
    components: {
      MainHeading,
      SubHeading
    }
  }
</script>
