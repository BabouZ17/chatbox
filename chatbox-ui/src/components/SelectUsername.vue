<template>
  <label for="username">Username to start chating: </label>
  <input
    type="text"
    name="username"
    v-on:keyup.enter="saveUsername"
    v-model="username"
    placeholder="Type your username"
  />
  <button @click="saveUsername">Submit</button>
</template>

<script>
export default {
  data() {
    return {
      username: ''
    }
  },
  methods: {
    saveUsername() {
      console.log(this.username)
      this.$router.push({ path: 'chat', query: { username: this.username } })
    }
  }
}
</script>