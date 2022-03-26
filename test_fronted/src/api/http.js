// 导入 axios
import axios from 'axios'

// 创建 axios 实例
var instance = axios.create({
  // 请求头
  headers: {
    'Content-Type': 'application/json'
  },
  // 基础 url，接口服务的地址
  baseURL: 'http://127.0.0.1:5000/',
  // 超时时间
  timeout: 2500
})

export default instance