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
                  v-model="darkMode"
                  label="Dark mode"
                ></v-switch>
          </v-card-text>
          
        </v-card>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-card>
          <v-card-title>Miscellaneous</v-card-title>
          <v-card-text>
            <v-switch
                  v-model="autoRefresh"
                  label="Auto refresh by 1 minute"
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
    },
    computed: {
      darkMode: {
        get () {
          return this.$store.state.darkMode
        },
        set () {
          this.$store.commit('switchDarkMode')
        }
      },
      autoRefresh: {
        get () {
          return this.$store.state.autoRefresh
        },
        set () {
          this.$store.commit('switchAutoRefresh')
        }
      },
    },
    watch: {
      darkMode (newValue) {
        localStorage.setItem('darkMode', newValue)
      },
      autoRefresh (newValue) {
        localStorage.setItem('autoRefresh', newValue)
      },
    },
    metaInfo: {
      title: 'Settings'
    },
  }
</script>
