from flask_sqlalchemy import SQLAlchemy

user_db = SQLAlchemy()


class Register(user_db.Model):
    __bind_key__ = 'user'
    __tablename__ = 'register'
    id = user_db.Column(user_db.Integer, primary_key=True, autoincrement=True)
    username = user_db.Column(user_db.String(32))  # 用户名
    password = user_db.Column(user_db.String(255))  # 密码
    email = user_db.Column(user_db.String(32))  # 邮箱
    creat_time = user_db.Column(user_db.Integer)  # 创建时间
    last_login = user_db.Column(user_db.Integer)  # 上次登入时间
    # telephon = user_db.Column(user_db.Integer)  #手机号
    status = user_db.Column(user_db.Integer)  # 状态
