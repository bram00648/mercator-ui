<template>
  <div>
    <input type="text" placeholder="example.be" v-model="domainName" />
    <button @click="submit">Submit</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      domainName: "",
    };
  },
  methods: {
    submit() {
      this.$emit("submit", this.domainName);
    },
  },
};
</script>
