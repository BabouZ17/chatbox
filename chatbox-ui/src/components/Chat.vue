<template>
  <div>
    <p>Welcome {{ username }} - Chat connected: {{ connected }}</p>
    <h2>Messages:</h2>
    <ul style="list-style-type: none">
      <li v-for="message in messages" :key="message.id">
        {{ message.sender }} : {{ message.content }}
      </li>
    </ul>

    <br />
    <div>
      <input
        type="text"
        v-on:keyup.enter="sendMessage"
        v-model="message"
        placeholder="Type your message here"
      />
      <button @click="sendMessage">Submit</button>
    </div>
  </div>
</template>

<script>
import { io } from 'socket.io-client'
import { v4 as uuidv4 } from 'uuid'

const socket = io('http://localhost:5000', { autoConnect: false })

export default {
  data() {
    return {
      connected: false,
      username: this.$route.query.username || 'default',
      message: '',
      messages: []
    }
  },

  mounted() {
    socket.on('connect', () => {
      this.connected = true
      socket.emit('begin_chat')

      let message = {
        id: uuidv4(),
        content: 'Joined the chat',
        sender: this.username
      }
      socket.emit('msg', message)
    })

    socket.on('disconnect', () => {
      this.connected = false

      let message = {
        id: uuidv4(),
        content: 'Left the chat',
        sender: this.username
      }

      socket.emit('msg', message)
      socket.emit('exit_chat')
    })

    socket.on('rsp', (msg) => {
      this.addMessages(msg)
    })

    this.connect()
  },
  methods: {
    connect() {
      socket.connect()
    },
    disconnect() {
      socket.disconnect()
    },
    sendMessage() {
      let message = {
        id: uuidv4(),
        content: this.message,
        sender: this.username
      }
      socket.emit('msg', message)

      this.addMessages(message)
      this.message = ''
    },
    addMessages(message) {
      this.messages.push(message)
    }
  },
  beforeDestroy() {
    this.disconnect()
  }
}
</script>
