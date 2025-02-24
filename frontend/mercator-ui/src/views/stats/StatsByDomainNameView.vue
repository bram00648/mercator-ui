<template>
  <div>
    <StatsSearchBarDomainName @submit="fetchStatsByDomainName" />
    <div v-if="stats.length">
      <h2>Results:</h2>
      <ul>
        <li v-for="stat in stats" :key="stat.visitId">
          {{ stat.visitId }} - {{ stat.web_domainName }}
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
        this.stats = await statsService.fetchAllTechnologyStatsByDomainName(
          domainName
        );
      } catch (error) {
        console.error("Error fetching stats by domain name:", error);
      }
    },
  },
};
</script>
