<template>
  <div class="stats-view">
    <h1>Technology Stats</h1>
    <Stats msg="All stats for all entries:" :stats="stats" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import StatsData from "@/components/stats/StatsData.vue";
import { Stat } from "@/types";
import statsService from "@/services/statsService";

@Options({
  components: {
    StatsData,
  },
})
export default class StatsView extends Vue {
  stats: Stat[] = [];

  async mounted() {
    try {
      this.stats = await statsService.fetchAllStats();
      console.log(this.stats);
    } catch (error) {
      console.error(error);
    }
  }
}
</script>
