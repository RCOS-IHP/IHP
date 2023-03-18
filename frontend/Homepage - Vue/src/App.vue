<template>
  <div id="app">
    <app-header></app-header>
    <app-hero></app-hero>
    <app-features></app-features>
    <ihp-footer></ihp-footer>
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppHero from "./components/AppHero.vue";
import AppFeatures from "./components/AppFeatures.vue";
import IhpFooter from "./components/IhpFooter.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppHero,
    AppFeatures,
    IhpFooter,
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

