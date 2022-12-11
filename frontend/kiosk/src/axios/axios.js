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
    console.log('axiousAuth')
    if (status === 401) {
      const originalConfig = config
      // token refresh 요청
      const { data } = await axios.post(
        `${store.state.axios_URL}/accounts/refresh/`, // token refresh api
        {
          user_id: store.state.userId,
          refresh: store.state.refresh,
        }
      )
      // 새로운 토큰 저장
      const newAccess = data.access
      store.state.acess = newAccess
      console.log('newAccessToken', newAccess)
      originalConfig.headers.Authorization = `Bearer ${newAccess}`
      // 401로 요청 실패했던 요청 새로운 accessToken으로 재요청
      return axios(originalConfig)
    }
    return Promise.reject(error)
  }
)

export default axiosAuth
