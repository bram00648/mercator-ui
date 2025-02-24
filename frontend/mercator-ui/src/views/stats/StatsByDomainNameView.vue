<template>
  <div>
    <StatsSearchBarDomainName @submit="fetchStatsByDomainName" />
    <div v-if="stats.length">
      <h2>Results:</h2>
      <ul>
        <li
          v-for="stat in stats"
          :key="stat.visitId"
          @click="push(stat.visitId)"
        >
          {{ stat.visitId }} - {{ stat.domainName }} - {{ stat.crawlFinished }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import StatsSearchBarDomainName from "@/components/stats/StatsSearchBarDomainName.vue";
import statsService from "@/services/statsService";

export default {
  components: {
    StatsSearchBarDomainName,
  },
  data() {
    return {
      stats: [],
    };
  },
  methods: {
    async fetchStatsByDomainName(domainName) {
      try {
        this.stats = await statsService.fetchAllIdsAndDataByDomainName(
          domainName
        );
      } catch (error) {
        console.error("Error fetching stats by domain name:", error);
      }
    },
    push(visitId) {
      this.$router.push({ name: "StatsByVisitIdView", params: { visitId } });
    },
  },
};
</script>
