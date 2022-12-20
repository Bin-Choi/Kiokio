<template>
  <div class="w-100 bg-white" style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />
    <div class="w-50 h-100 m-auto" style="font-size: 3.5vh; padding-top: 5vh">
      <!-- STUDENT -->
      <div class="admin-btn-box rounded shadow row">
        <span class="col-5">학생관리</span>
        <div
          @click="$router.push({ name: 'student' })"
          class="admin-view-button shadow col-4">
          <font-awesome-icon icon="fa-solid fa-caret-right" /> 학생 조회
        </div>
      </div>

      <!-- ATTENDANCE -->
      <div class="admin-btn-box rounded shadow row">
        <span class="col-5">출결관리</span>
        <div
          @click="$router.push({ name: 'attendance' })"
          class="admin-view-button shadow col-4">
          <font-awesome-icon icon="fa-solid fa-caret-right" /> 출결 조회
        </div>
      </div>

      <!-- INBODY -->
      <div class="admin-btn-box rounded shadow row">
        <span class="col-5"> 인바디관리</span>

        <div
          class="col-6 d-flex justify-content-evenly"
          style="font-size: 2.5vh; cursor: pointer">
          <div
            @click="$router.push({ name: 'adminInbody' })"
            class="admin-view-button shadow">
            <font-awesome-icon icon="fa-solid fa-caret-right" /> 기간으로 조회
          </div>
          <div
            @click="$router.push({ name: 'adminInbodyDate' })"
            class="admin-view-button shadow">
            <font-awesome-icon icon="fa-solid fa-caret-right" /> 특정 날짜로
            조회
          </div>
        </div>
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

  width: fit-content;
  height: 8vh;
  padding: 1vh 1.5vh;
  line-height: 6vh;
  border-radius: 5vh;
}

.admin-btn-box {
  background-color: #81a0bb4b;
  margin: 2vh 0;
  padding: 2vh;

  height: 25%;
  display: flex;
  align-items: center;
  justify-content: center;
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
