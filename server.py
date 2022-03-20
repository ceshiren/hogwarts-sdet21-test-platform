"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)


# with open("./data.yml") as f:
#     result = yaml.safe_load(f)
username = "root"
password = "1qaz9ol."
server = "134.175.28.202"
db = "ck21"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)

# 导包
def get_router():
    from router.testcase import case_ns
    api.add_namespace(case_ns, "/testcase")

if __name__ == '__main__':
    # 调用getrouter方法，完成testcase 路由的注册
    get_router()
    app.run(debug=True)