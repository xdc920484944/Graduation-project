from app.models.lagou import lg_db
from app.models.user import user_db
from app.models.wuyou import wy_db
from app.models.zhilian import zl_db
from app.models.tc import tc_db


def creat_db(app):
    '''
    创建数据库表单
    :return:
    '''
    wy_db.init_app(app)
    wy_db.create_all(app=app)
    # lg_db.init_app(app)
    # lg_db.create_all(app=app, bind='lagou')
    zl_db.init_app(app)
    zl_db.create_all(app=app, bind='zhilian')
    user_db.init_app(app)
    user_db.create_all(app=app, bind='user')
    tc_db.init_app(app)
    tc_db.create_all(app=app, bind='tc')

