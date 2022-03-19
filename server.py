"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

import yaml
from flask import Flask, request
from flask_restx import Resource, Api, Namespace
from flask_sqlalchemy import SQLAlchemy
# 实例化app 对象
from sqlalchemy import *

from backend_actual.log_util import logger

app = Flask(__name__)
api = Api(app)
# 用例的命名空间

with open("./data.yml") as f:
    result = yaml.safe_load(f)
    username = result.get("database").get('username')
    password = result.get("database").get('password')
    server = result.get("database").get('server')
    db = result.get("database").get('db')

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)

def get_router():
    from router.testcase import case_ns
    api.add_namespace(case_ns, "/testcase")

if __name__ == '__main__':
    get_router()
    app.run(debug=True)