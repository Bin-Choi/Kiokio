<template>
  <div class="pt-5">
    <div
      id="title"
      class="w-75 m-auto bg-primary rounded text-light p-1"
      style="font-size: 90px"
    >
      인바디 등록하기
    </div>
    <div class="w-75 bg-light rounded m-auto my-3 py-3 px-2">
      <p>0 학년 0 반 이름 000</p>
      <div class="d-flex">
        <p>검사일시</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="검사일시"
          v-model.trim="number"
          maxlength="6"
          minlength="6"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>키</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="키"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>나이</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="나이"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>성별</p>
        <div class="radio">
          <input type="radio" name="gender" value="man" />남
          <input type="radio" name="gender" value="woman" />여
        </div>
      </div>
      <div class="d-flex">
        <p>체수분</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="체수분"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>단백질</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="단백질"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>무기질</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="무기질"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>체지방량</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="키"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>체중</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="체중"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>골격근량</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="골격근량"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>체지방량</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="체지방량"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>BMI</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="BMI"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <P> 체지방률</P>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="체지방률"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
      <div class="d-flex">
        <p>인바디점수</p>
        <input
          type="text"
          id="datepicker_init_day"
          placeholder="인바디점수"
          v-model.trim="number"
          class="rounded bg-light m-2"
        />
      </div>
    </div>

    <!-- BUTTONS -->
    <button
      type="button"
      class="btn btn-primary m-1"
      @click="$router.push({ name: 'inbodyForm' })"
    >
      등록하기
    </button>
    <div class="w-25 d-flex m-2 align-items-center" @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>
  </div>
</template>

<script>
export default {
  name: "InbodyFormView",
}
</script>

<style scoped>
[type="radio"] {
  vertical-align: middle;
  appearance: none;
  border: max(2px, 0.1em) solid gray;
  border-radius: 50%;
  width: 1.25em;
  height: 1.25em;
  transition: border 0.5s ease-in-out;
}

[type="radio"]:checked {
  border: 0.4em solid tomato;
}

[type="radio"]:focus-visible {
  outline-offset: max(2px, 0.1em);
  outline: max(2px, 0.1em) dotted tomato;
}
</style>
