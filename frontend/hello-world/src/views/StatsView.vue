<script setup>
import { ref, onMounted } from "vue";
import { getStats } from "@/api/stats"; // Import the API function"

const stats = ref([]);

onMounted(async () => {
  stats.value = await getStats();
});
</script>

<template>
  <div>
    <h1>Stats</h1>
    <ul v-if="stats.length">
      <li v-for="(item, index) in stats" :key="index">
        <strong>{{ item.domain_name }}</strong> - {{ item.detected_technologies.join(", ") }}
      </li>
    </ul>
    <p v-else>Loading stats...</p>
  </div>
</template>

<style scoped>
h1 {
  color: #42b983;
}
</style>
