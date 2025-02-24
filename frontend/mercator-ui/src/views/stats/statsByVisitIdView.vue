<template>
  <div>
    <h2>Visit Stats for {{ visitId }}</h2>
    <div v-if="visitStats">
      <pre>{{ visitStats }}</pre>
    </div>
  </div>
</template>

<script>
import statsService from "@/services/statsService";

export default {
  props: ["visitId"],
  data() {
    return {
      visitStats: null,
    };
  },
  async created() {
    try {
      this.visitStats = await statsService.fetchAllTechnologyStatsByVisitId(
        this.visitId
      );
    } catch (error) {
      console.error("Error fetching stats by visit ID:", error);
    }
  },
};
</script>
