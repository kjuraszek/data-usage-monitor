<template>
    <v-main class="grey lighten-3">
        <v-slide-x-transition mode="out-in">
            <router-view />
        </v-slide-x-transition>
    </v-main>
</template>

<script>
export default {
    name: 'Main',
}
</script>