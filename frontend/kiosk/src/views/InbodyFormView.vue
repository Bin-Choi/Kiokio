<template>
  <div>
    <!-- BACK -->
    <div
      class="d-flex"
      @click="$router.go(-1)"
      style="font-size: 4.5vh; margin: 3vh; margin-bottom: 1vh"
    >
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <div
      class="h-100 d-flex flex-column justify-content-between align-items-center"
      style="padding: 2vh 0"
    >
      <!-- PAGE TITLE -->
      <div
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 5vh"
      >
        인바디 등록
      </div>

      <div style="font-size: 3vh">0학년 0반 학생이름</div>

      <!-- INBODY FORM -->
      <div
        class="w-75 bg-light rounded shadow"
        style="font-size: 2.5vh; padding: 2.5vh 2vh; height: 60vh"
      >
        <div id="scroll-box" class="container" style="height: 100%">
          <div class="row">
            <p class="col">검사일시</p>
            <input type="date" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">키</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">나이</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">체수분</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">단백질</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">무기질</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">체지방량</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">체중</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">골격근량</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">BMI</p>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <P class="col">체지방률</P>
            <input type="text" class="rounded col" />
          </div>

          <div class="row">
            <p class="col">인바디점수</p>
            <input type="text" class="rounded col" />
          </div>
        </div>
      </div>
      <!-- BUTTON -->
      <button
        type="button"
        class="btn btn-primary shadow"
        style="font-size: 3vh; padding: 0.5vh"
        @click="$router.push({ name: 'inbodyForm' })"
      >
        등록하기
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InbodyFormView',
}
</script>

<style scoped>
.row {
  margin: 1vh 0;
}

input {
  margin-right: 1.5vh;
  height: 5vh;
  background: none;
  border: 0.2vh solid #2b64aa1e;
  border-radius: 0.5vh;
  box-shadow: 0.1vh 0.1vh 0.1vh #2b64aa1e;
}
</style>
