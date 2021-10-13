<template>
  <section class="relative w-full h-screen">
    <section class="flex flex-col justify-center items-center w-full">
      <div class="flex justify-center">
        <img src=".././assets/lihim-logo.png" alt="lihim logo" class="w-1/2" />
      </div>
      <div class="flex space-x-5">
        <User
          v-for="(user, key) in users"
          :key="key"
          :username="user"
          @click="openPasswordModal(user)"
        />
      </div>
    </section>
    <PasswordModal
      :username="userSelected"
      v-show="togglePasswordModal"
      @close="togglePasswordModal = false"
    />
  </section>
</template>

<script>
import User from "./User.vue";
import axios from "../utils/axios";
import PasswordModal from "./PasswordModal.vue";

export default {
  components: { User, PasswordModal },
  data() {
    return {
      users: null,
      togglePasswordModal: false,
      userSelected: null,
    };
  },
  created() {
    axios.get("/api/users").then((response) => {
      this.users = response.data.content;
    });
  },
  methods: {
    openPasswordModal(user) {
      this.userSelected = user;
      this.togglePasswordModal = true;
    },
  },
};
</script>

<style>
</style>