import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import StatsByDomainNameView from "../views/stats/StatsByDomainNameView.vue";
import StatsView from "../views/stats/StatsView.vue";
import statsByVisitIdView from "@/views/stats/statsByVisitIdView.vue";
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/stats",
    name: "stats",

    component: StatsView,
  },

  {
    path: "/stats/By-Domain-Name",
    name: "statsByDomainName",
    component: StatsByDomainNameView,
  },

  {
    path: "/stats/by-visit-id/:visitId",
    name: "StatsByVisitIdView",
    component: statsByVisitIdView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
