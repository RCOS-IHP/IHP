<template>
  
  <div id="app">
    <app-header></app-header>
    <app-hero></app-hero>
    <app-features></app-features>
    <app-footer></app-footer>
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppHero from "./components/AppHero.vue";
import AppFeatures from "./components/AppFeatures.vue";
import AppFooter from "./components/AppFooter.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppHero,
    AppFeatures,
    AppFooter,
  },
};
</script>

<style>
body {
  font-family: "Arial", sans-serif;
  margin: 0;
  padding: 0;
  background-color: #ffffff;
}
</style>
