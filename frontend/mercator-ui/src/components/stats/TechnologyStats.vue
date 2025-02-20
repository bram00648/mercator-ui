<template>
    <div class="technologyStats">
      <h1>{{ msg }}</h1>
      <p>The following Technologies were detected for visitId: x</p>
     <ul v-if="!detected_technologies.length">
        <li></li>
        <<li v-for="tech in detected_technologies" :key="tech">{{ tech }}</li>


     </ul>
    </div>
  </template>
  
  <script lang="ts">
  import { Options, Vue } from "vue-class-component";
  
  @Options({
    props: {
      msg: String,
    },
  })
  export default class TechnologyStats extends Vue {
    msg!: string;
    detected_technologies!: string[];
    visit_id!: string;
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  