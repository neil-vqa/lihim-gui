<template>
  <section class="flex flex-col justify-center items-center w-full">
    <div class="flex justify-center">
      <img src=".././assets/lihim-logo.png" alt="lihim logo" class="w-1/2" />
    </div>
    <div class="flex space-x-5">
      <User v-for="(user, key) in users" :key="key" :username="user" />
    </div>
  </section>
</template>

<script>
import User from "./User.vue";
import axios from "../utils/axios";

export default {
  components: { User },
  data() {
    return {
      users: null,
    };
  },
  created() {
    axios.get("/api/users").then((response) => {
      this.users = response.data.content;
    });
  },
};
</script>

<style>
</style>