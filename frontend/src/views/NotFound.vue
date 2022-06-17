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
  import { GoBackButton, MainHeading, SubHeading } from '@/partials'

  export default {
    name: "NotFound",
    data: () => ({
      mainTitle: "Page Not Found",
      subTitle: "Nothing found under this URL - check if URL is correct or return to home.",
    }),
    components: {
      GoBackButton,
      MainHeading,
      SubHeading
    }
  }
</script>
