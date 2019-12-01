from flask import Blueprint
#蓝图初始化
web = Blueprint("web", __name__)
import app.web.home
