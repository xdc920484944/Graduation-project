from flask import Flask
from app.web import web
from app.models import creat_db


def creat_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 表单创建
    creat_db(app)


    # 蓝图注册
    # app.register_blueprint(admin)
    app.register_blueprint(web)

    return app
