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
            cols="12"
            md="6"
          >
            <v-card>
              <v-card-title>Data Usage</v-card-title>
              <v-card-text>
                <v-slide-y-transition mode="out-in">
                  <Loader
                    v-if="loading"
                    text="Fetching the data"
                  ></Loader>
                  <UsageDataTable v-else />
                </v-slide-y-transition>               
              </v-card-text>
            </v-card>
          </v-col>
          <v-col
            cols="12"
            md="6"
          >
            <v-card>
              <v-card-title>Status</v-card-title>
              <v-card-text>
                <v-switch
                  v-model="loading"
                  label="Loading"
                ></v-switch>
                <v-slide-y-transition mode="out-in">
                  <div class="text-left">
                    <div v-if="loading">
                      <v-icon
                        size="30"
                        color="info"
                      >
                      mdi-reload
                      </v-icon>
                      Loading
                    </div>
                    <div v-else>
                      <v-icon
                      size="30"
                      color="success"
                      >
                      mdi-check-circle-outline
                      </v-icon>
                      Success
                    </div>
                  </div>
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
  import { MainHeading, SubHeading, Loader, Failed, UsageDataTable } from "@/partials"

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
      Failed,
      UsageDataTable
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
    metaInfo: {
      title: 'Home'
    },
  }
</script>
