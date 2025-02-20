<template>
  <div class="stats-view">
    <h1>Technology Stats</h1>
    <img alt="Vue logo" src="../assets/logo.png" />
    <TechnologyStats
      msg="stats of all technologies for given id"
      :detected_technologies="stats?.detected_technologies"
    />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import TechnologyStats from "@/components/stats/TechnologyStats.vue";
import { TechnologyStat } from "@/types";
import statsService from "@/services/statsService";

@Options({
  components: {
    TechnologyStats,
  },
})
export default class StatsView extends Vue {
  stats: TechnologyStat | null = null;

  async mounted() {
    try {
      this.stats = await statsService.fetchAllTechnologyStats();
      console.log(this.stats);
    } catch (error) {
      console.error(error);
    }
  }
}
</script>
