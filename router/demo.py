"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import json

if __name__ == '__main__':
    data = "[3]"
    # data2 = [3]
    for i in data:
        print(i)

    for j in json.loads(data):
        print(j)
