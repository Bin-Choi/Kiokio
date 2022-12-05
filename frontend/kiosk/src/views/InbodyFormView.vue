<template>
  <div class="h-100 d-flex flex-column justify-content-between">
    <div
      class="w-75 m-auto bg-primary rounded text-light p-1 shadow"
      style="font-size: 3em"
    >
      인바디 등록하기
    </div>

    <div>0 학년 0 반 이름 000</div>

    <div class="w-75 bg-light rounded m-auto shadow container p-5">

      <div class="row">
        <p class="col">검사일시</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="검사일시"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">키</p>
        <input
          type="text"
          placeholder="키"
          v-model.trim="number"
          class="rounded bg-light m-2 col"
        />
      </div>

      <div class="row">
        <p class="col">나이</p>
        <input
          type="text"
          placeholder="나이"
          v-model.trim="number"
          class="rounded bg-light m-2 col"
        />
      </div>
      
      <div class="row">
        <p class="col">체수분</p>
        <input
          type="text"
          placeholder="체수분"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">단백질</p>
        <input
          type="text"
          placeholder="단백질"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">무기질</p>
        <input
          type="text"
          placeholder="무기질"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">체지방량</p>
        <input
          type="text"
          placeholder="키"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">체중</p>
        <input
          type="text"
          placeholder="체중"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">골격근량</p>
        <input
          type="text"
          placeholder="골격근량"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">체지방량</p>
        <input
          type="text"
          placeholder="체지방량"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="d-flex">
        <p class="col">BMI</p>
        <input
          type="text"
          placeholder="BMI"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="d-flex">
        <P class="col">체지방률</P>
        <input
          type="text"
          placeholder="체지방률"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>

      <div class="row">
        <p class="col">인바디점수</p>
        <input
          type="text"
          placeholder="인바디점수"
          v-model.trim="number"
          class="rounded bg-light col"
        />
      </div>
    </div>

    <!-- BUTTON -->
    <button
      type="button"
      class="btn btn-primary m-auto p-3 shadow" style="font-size:2em;"
      @click="$router.push({ name: 'inbodyForm' })"
    >
      등록하기
    </button>

    <!-- BACK -->
    <div class="d-flex m-5 align-items-center" style="font-size:2em;"
    @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>

  </div>
</template>

<script>
export default {
  name: "InbodyFormView",
}
</script>

<style>

</style>
