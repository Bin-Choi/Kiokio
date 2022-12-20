<template>
  <div class="w-100 bg-white" style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />
    <div
      class="w-50 m-auto h-75 d-flex flex-column justify-content-center align-items-center"
      style="padding-top: 5vh; min-width: 1310px"
    >
      <!-- STUDENT -->
      <div
        @click="$router.push({ name: 'student' })"
        class="admin-view-button shadow"
      >
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 학생 관리
      </div>

      <!-- ATTENDANCE -->

      <div
        @click="$router.push({ name: 'attendance' })"
        class="admin-view-button shadow"
      >
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 출결 관리
      </div>

      <!-- INBODY -->

      <div
        @click="$router.push({ name: 'adminInbody' })"
        class="admin-view-button shadow"
      >
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 기간으로 인바디
        조회
      </div>
      <div
        @click="$router.push({ name: 'adminInbodyDate' })"
        class="admin-view-button shadow"
      >
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 특정 날짜로 인바디
        조회
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'

export default {
  name: 'AdminView',
  components: {
    AdminHeader,
  },
}
</script>

<style>
#content {
  min-width: 550px;
}
.student-search-form {
  background-color: white;
  margin: 0 1.5vh 0 0.5vh;
  width: 10vh;
  height: 3.5vh;
  border-radius: 1vh;
}
.admin-view-button {
  color: white;
  background-color: #6396c3;
  cursor: pointer;

  width: 10%;
  min-width: 300px;
  height: 10vh;

  margin: 1.5vh 0;
  padding: 1vh;
  line-height: 8vh;
  border-radius: 5vh;
  font-size: 3vh;
}

.green-btn,
.blue-btn,
.red-btn,
.gray-btn {
  width: fit-content;
  height: 3.5vh;
  border-radius: 1vh;
  border: 0;
  color: white;
  font-size: 1.8vh;
}

.red-btn:focus,
.blue-btn:focus,
.green-btn:focus,
.gray-btn:focus {
  outline: 2px solid black;
}

.green-btn {
  background-color: rgb(109, 163, 28);
  margin-left: 1vh;
}
.red-btn {
  background-color: rgb(193, 32, 42);
}
.blue-btn {
  background-color: #6396c3;
}
.gray-btn {
  background-color: rgb(121, 121, 121);
}

.gray-btn:hover {
  background-color: rgb(66, 66, 66);
}
.green-btn:hover {
  background-color: rgb(89, 96, 19);
}
.red-btn:hover {
  background-color: rgb(123, 18, 18);
}
.blue-btn:hover {
  background-color: rgb(18, 28, 115);
}

#admin-scroll-box {
  height: 60vh;
  overflow: auto;
}

#admin-scroll-box::-webkit-scrollbar {
  height: 1vh;
  width: 1vh;
  margin: 1vh;
}
#admin-scroll-box::-webkit-scrollbar-thumb {
  background-color: #6396c3;
  border-radius: 0.5vh;
}

#admin-scroll-box::-webkit-scrollbar-corner {
  display: none;
}
</style>
