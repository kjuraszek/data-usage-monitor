<template>
  <v-container>
    <v-row class="text-center">

      <v-col class="my-10">
        <MainHeading
          :text="mainTitle"
        ></MainHeading>

        <SubHeading
          :text="subTitle"
        ></SubHeading>

      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-9">
          Current data usage
        </h2>

        <v-row>
          <v-col
            v-for="n in 3"
            :key="n"
            cols="12"
            sm="6"
            md="3"
          >
            <v-card>
              <v-card-title>Data Usage #{{ n }}</v-card-title>
              <v-card-text>
                <v-progress-circular
                  :rotate="270"
                  :size="150"
                  :width="25"
                  :value="52*n % 99"
                  :color="`green darken-${n}`"
                >
                  
                </v-progress-circular>

                <p class="text-h5">{{ 52*n % 99 }}%</p>
                
              </v-card-text>
              
            </v-card>
          </v-col>
          
          <v-col
            cols="12"
            sm="6"
            md="3"
          >
            <v-card>
              <v-card-title>Status</v-card-title>
              <v-card-text>
                <v-switch
                  v-model="loading"
                  label="Switch 1"
                ></v-switch>
                <v-slide-y-transition mode="out-in">
                  <Loader
                      v-if="loading"
                      text="Fetching the data"
                    ></Loader>
                    <Failed
                      v-else
                      text="Failed"
                    ></Failed>
                    
                </v-slide-y-transition>
                
                
              </v-card-text>
              
            </v-card>
          </v-col>
          
        </v-row>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import { MainHeading, SubHeading, Loader, Failed } from "@/partials"

  export default {
    name: "Home",
    data: () => ({
      mainTitle: "Home",
      subTitle: "Welcome to the Data Usage Monitor dashboard. You can see here a basic informations about the data transfer of your network (based on the data harvested from router).",
    }),
    components: {
      MainHeading,
      SubHeading,
      Loader,
      Failed
    },
    computed: {
      loading: {
        get () {
          return this.$store.state.loading
        },
        set () {
          this.$store.commit('switchLoading')
        }
      }
    },
  }
</script>
