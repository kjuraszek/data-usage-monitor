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

        <GoBackButton />
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import { GoBackButton, MainHeading, SubHeading } from "@/partials"

  export default {
    name: "WorkInProgress",
    data: () => ({
      mainTitle: "Work In Progress",
      subTitle: "This page is currently blank but it will change soon!",
    }),
    components: {
      GoBackButton,
      MainHeading,
      SubHeading
    }
  }
</script>
