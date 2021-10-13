<template>
  <section
    class="
      absolute
      top-0
      z-10
      w-full
      h-full
      bg-white
      flex
      items-center
      justify-center
      bg-opacity-95
    "
  >
    <section class="w-96 space-y-8">
      <div class="text-right">
        <button
          @click="closeModal"
          class="p-2 rounded-full bg-red-400 text-white"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="icon icon-tabler icon-tabler-x"
            width="30"
            height="30"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            fill="none"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </div>
      <div class="bg-white rounded-xl shadow-2xl px-8 py-4 text-center">
        <h2 class="font-bold text-5xl">{{ username }}</h2>
      </div>
      <div class="bg-white rounded-xl shadow-2xl px-8 py-4">
        <form @submit.prevent="login" class="space-y-4">
          <div class="flex flex-col">
            <label class="text-xs my-2">Password</label>
            <input
              type="password"
              v-model="password"
              class="bg-gray-100 px-3 py-2 rounded-lg"
              required
            />
            <label class="text-xs my-2">Key File</label>
            <input
              type="text"
              v-model="key"
              class="bg-gray-100 px-3 py-2 rounded-lg"
              required
            />
          </div>
          <button
            type="submit"
            class="
              bg-gray-500
              px-3
              py-3
              w-full
              uppercase
              text-xs text-white
              rounded-lg
              hover:bg-gray-900
            "
          >
            login
          </button>
        </form>
      </div>
    </section>
  </section>
</template>

<script>
import axios from "../utils/axios";

export default {
  props: {
    username: String,
  },
  data() {
    return {
      password: null,
      key: null,
    };
  },
  methods: {
    closeModal() {
      this.password = null;
      this.key = null;
      this.$emit("close");
    },
    login() {
      console.log(this.password);
      console.log(this.key);

      axios
        .post("/api/login", {
          username: this.username,
          password: this.password,
          key: this.key,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
</style>