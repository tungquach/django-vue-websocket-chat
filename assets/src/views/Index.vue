<template>
  <div class="wrapper">
    <div class="container">
      <div class="left">
        <div class="top">
          <input
            v-model="roomName"
            type="text"
            placeholder="What chat room would you like to enter?"
          />
          <button
            class="search"
            @click="enterRoom(roomName)"
          >Enter</button>
        </div>
        <ul class="people">
          <li
            v-for="(_, room) in listRoomEntered"
            :key="room"
            class="person"
            :class="{active: room === roomNameEntered}"
            @click="enterRoom(room)"
          >
            <span class="name">#{{ room }}</span>
          </li>
        </ul>
      </div>
      <div class="right">
        <ChatRoom
          v-if="roomNameEntered"
          :roomName="roomNameEntered"
        />
        <p
          class="notice"
          v-else
        >Enter a room to chat!</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import ChatRoom from "@/components/ChatRoom.vue";

@Component({
  components: {
    ChatRoom
  }
})
export default class App extends Vue {
  roomName: string = "";
  roomNameEntered: string = "";
  listRoomEntered: { [key: string]: 1 } = {};

  enterRoom(name: string): void {
    this.roomNameEntered = "";
    this.roomName = "";
    setTimeout(() => {
      this.roomNameEntered = name;
      this.listRoomEntered[name] = 1;
    }, 100);
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/app.scss";
</style>