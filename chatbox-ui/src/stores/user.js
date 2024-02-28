import { defineStore } from 'pinia'


export const useStore = defineStore('user', {
  state: () => {
    return { username: "", messages: [] }
  },
  actions: {
    setUsername(name) {
      this.username = name
    }
  }
})
