// 导入配置好的 axios 实例
import axios from './http'

const testcase = {
  // 获取用例
  getTestcase(params){
    return axios({
      method: 'get',
      url: '/testcase',
      // get 请求需要通过 url 拼接请求参数
      params: params
    })
  },
  // 添加用例
  addTestcase(data){
    return axios({
      method: 'post',
      url: '/testcase',
      // 如果是传递请求体，需要使用 data 来传参
      data: data
    })
  },
  // 删除用例
  deleteTestcase(params){
    return axios({
      method: 'delete',
      url: '/testcase',
      params: params
    })
  },
  // 修改用例
  updateTestcase(data) {
    return axios({
      method: 'put',
      url: '/testcase',
      data: data
    })
  }
}

export default testcase