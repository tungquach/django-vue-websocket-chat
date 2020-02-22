<template>
  <div>
    <div class="top"><span><span class="name">#{{ roomName }}</span></span></div>
    <div class="chat active-chat">
      <div class="conversation-start">
        <span>Today, 6:48 AM</span>
      </div>
      <div
        v-for="(message, index) in messages"
        :key="index"
        class="bubble text"
      >
        {{ message }}
      </div>
    </div>
    <div class="write">
      <a
        href="javascript:;"
        class="write-link attach"
      ><i class="fas fa-paperclip"></i></a>
      <input
        type="text"
        @keyup.enter="sendMessage()"
        v-model="message"
        placeholder="Send a message..."
      />
      <a
        @click="sendMessage()"
        href="javascript:;"
        class="write-link send"
      >
        <i class="far fa-paper-plane"></i>
      </a>
      <a
        href="javascript:;"
        class="write-link smiley"
      >
        <i class="far fa-smile"></i>
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class ChatRoom extends Vue {
  @Prop() private roomName!: string;

  messages: Array<string> = [];
  chatSocket: WebSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${this.roomName}/`
  );
  message: string = "";

  mounted() {
    this.chatSocket.onmessage = e => {
      const data = JSON.parse(e.data);
      const message = data.message;
      this.messages.push(message);
    };

    this.chatSocket.onclose = e => {
      console.error("chat socket closed unexpectedly!");
    };
  }

  sendMessage(): void {
    this.chatSocket.send(
      JSON.stringify({
        message: this.message
      })
    );

    this.message = "";
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/app.scss";
</style>