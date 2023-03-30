<template>
  <div class="w-100 bg-white" style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />
    <div
      class="w-50 m-auto h-75 d-flex flex-column justify-content-center align-items-center"
      style="padding-top: 5vh; min-width: 1310px"
    >
      <!-- STUDENT -->
      <div
        @click="() => $router.push({ name: 'student' })"
        class="admin-view-button shadow"
      >
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 학생 관리
      </div>

      <!-- ATTENDANCE -->

      <div
        @click="() => $router.push({ name: 'attendance' })"
        class="admin-view-button shadow"
      >
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 출결 관리
      </div>

      <!-- INBODY -->

      <div class="inbody admin-view-button shadow">
        <font-awesome-icon icon="fa-solid fa-caret-right" /> 인바디 관리
        <div class="inbody__buttons">
          <button
            class="shadow"
            @click="() => $router.push({ name: 'adminInbody' })"
          >
            기간으로 조회
          </button>
          <button
            class="shadow"
            @click="() => $router.push({ name: 'adminInbodyDate' })"
          >
            특정 날짜로 조회
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/admin/common/AdminHeader.vue'

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
/* .student-search-form {
  background-color: white;
  margin: 0 1.5vh 0 0.5vh;
  width: 10vh;
  height: 3.5vh;
  border-radius: 1vh;
} */
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
  border-radius: 3vh;
  font-size: 3vh;
}

.inbody__buttons {
  display: flex;
  justify-content: space-evenly;

  font-size: 2vh;
}

.inbody__buttons > button {
  color: white;
  background-color: #6396c3;
  cursor: pointer;
  height: 6vh;
  line-height: 2vh;

  border: none;
  border-radius: 2vh;

  margin: 3vh 0;

  visibility: hidden;
}

.inbody:hover > .inbody__buttons > button {
  visibility: visible;
}

.buttons {
  display: flex;
  justify-content: flex-end;
  margin: 0.5vh 0;
}

.buttons > button {
  margin-left: 0.5vh;
}

#admin-scroll-box {
  height: 60vh;
  overflow: auto;
}

#admin-scroll-box::-webkit-scrollbar {
  height: 0.7vh;
  width: 0.7vh;
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
