<template>
    <v-main class="secondary">
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