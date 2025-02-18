import { createRouter, createWebHistory } from "vue-router";
import StatsView from "../components/StatsView.vue";

const routes = [
  { path: "/", redirect: "/stats" },  // Default route
  { path: "/stats", component: StatsView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
