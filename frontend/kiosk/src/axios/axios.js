import axios from 'axios'
import store from '@/store/index.js'

const axiosAuth = axios.create()

axiosAuth.interceptors.response.use(
  function (response) {
    // 2xx 범위에 있는 상태 코드는 이 함수를 트리거 합니다.
    // 응답 데이터가 있는 작업 수행
    return response
  },
  // async 내부에서만 await 사용가능
  async function (error) {
    // 2xx 외의 범위에 있는 상태 코드는 이 함수를 트리거 합니다.
    // 응답 오류가 있는 작업 수행
    const {
      config,
      response: { status },
    } = error
    if (status === 401) {
      const originalConfig = config
      // token refresh 요청
      await axios
        .post(
          `${store.state.axios_URL}/accounts/refresh/`, // token refresh api
          {
            user_id: store.state.user.id,
            refresh: store.state.refresh,
          }
        )
        .then((res) => {
          console.log(res)
          // 새로운 토큰 발급 성공
          console.log('refresh access token')
          const newAccess = res.data.access
          store.state.access = newAccess
          originalConfig.headers.Authorization = `Bearer ${newAccess}`
          // 401로 요청 실패했던 요청 새로운 accessToken으로 재요청
          return axiosAuth(originalConfig)
        })
        .catch(() => {
          // refresh 토큰이 문제일 경우, 로그인 창 뜨게 만들기(로그아웃이 아닐 경우)
          if (!originalConfig.url.slice(-7) === 'logout/') {
            alert('로그인 후 다시 시도해주세요')
            store.commit('TOGGLE_SHOW_LOGIN_MODAL', true)
          }
        })
    }
    return Promise.reject(error)
  }
)

export default axiosAuth
