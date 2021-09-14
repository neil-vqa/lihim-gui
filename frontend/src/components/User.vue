<template>
  <section
    class="
      rounded-full
      cursor-pointer
      fill-current
      text-black
      hover:text-white
      hover:bg-black
    "
  >
    <svg
      class="w-40 h-40"
      fill="none"
      stroke="currentColor"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="1"
        d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"
      ></path>
    </svg>
    <p class="text-3xl text-center pt-5 pb-10">{{ username }}</p>
  </section>
</template>

<script>
export default {
  props: {
    username: String,
  },
};
</script>

<style>
</style>