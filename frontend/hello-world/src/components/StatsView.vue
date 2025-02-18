<template>
  <div>
    <h2>Stats Data</h2>
    <table v-if="stats.length">
      <thead>
        <tr>
          <th>Visit ID</th>
          <th>Domain</th>
          <th>Technologies</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stat in stats" :key="stat.visit_id">
          <td>{{ stat.visit_id }}</td>
          <td>{{ stat.domain_name }}</td>
          <td v-if="stat.detected_technologies">{{ stat.detected_technologies.join(", ") }}</td>
          <td v-else>N/A</td>
        </tr>
      </tbody>
    </table>
    <p v-else>Loading stats...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { fetchStats } from "../services/statsService";

const stats = ref([]);

onMounted(async () => {
  stats.value = await fetchStats();
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>