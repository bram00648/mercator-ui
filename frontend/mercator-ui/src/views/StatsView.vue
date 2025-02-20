<template>
    <div class="Stats">
      <p style="color: red; font-size: 20px;">testing</p>
      
      <!-- Pass the fetched data to TechnologyStats component -->
      <TechnologyStats 
        msg="Welcome to Your Vue.js + TypeScript App" 
        :technologies="technologies"
        :this.visit_id="visit_id" 
      />
    </div>
</template>
  
<script lang="ts">
  import { Options, Vue } from "vue-class-component";
  import TechnologyStats from "@/components/stats/TechnologyStats.vue";
  import statsService from "@/services/statsService";
  import { TechnologyStat } from "@/types";
  
  @Options({
    components: {
      TechnologyStats,
    },
  })


  export default class StatsView extends Vue {
    technologies: TechnologyStat["detected_technologies"] = []; // reactive
    visit_id: TechnologyStat["visit_id"] = "";
  
    async fetchTechnologies() {
      try {
        const data = await statsService.fetchAllTechnologyStats(1); 
        this.technologies = data.detected_technologies;

      } catch (error) {
        console.error("Error fetching technology stats:", error);
      }
    }
  
    // Fetch data when the page is loaded
    mounted() {
      this.fetchTechnologies();
    }
  }
</script>
  