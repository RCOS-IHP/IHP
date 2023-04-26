import Vue from "vue";
import Router from "vue-router";
import AboutUsPage from "./components/AboutUsPage.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/aboutus",
      name: "AboutUsPage",
      component: AboutUsPage,
    },
  ],
});