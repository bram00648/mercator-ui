<template>
  <div>
    <h2>{{ msg }}</h2>
    <ul>
      <li v-for="stat in stats" :key="stat.visitId">
        {{ stat.visitId }} - {{ stat.web_domainName }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { TechnologyStat } from "@/types";

export default defineComponent({
  props: {
    msg: String,
    stats: {
      type: Array as PropType<TechnologyStat[]>,
      required: true,
    },
  },
});
</script>
