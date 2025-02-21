<template>
  <div class="stats-view">
    <h1>Technology Stats</h1>
    <TechnologyStats msg="All stats for all entries:" :stats="stats" />
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
  stats: TechnologyStat[] = [];

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
