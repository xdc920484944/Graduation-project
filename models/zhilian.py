from flask_sqlalchemy import SQLAlchemy

zl_db = SQLAlchemy()


class Zhilian(zl_db.Model):
    __bind_key__ = 'zhilian'
    __tablename__ = 'data'
    id = zl_db.Column(zl_db.Integer, primary_key=True, autoincrement=True)
    key = zl_db.Column(zl_db.String(10))  # 搜索职业
    city = zl_db.Column(zl_db.String(10))  # 搜索城市
    occupation = zl_db.Column(zl_db.String(50))  # 职业
    company_name = zl_db.Column(zl_db.String(30))  # 公司名字
    address = zl_db.Column(zl_db.String(30))  # 地址
    salary = zl_db.Column(zl_db.String(30))  # 薪资
    release_time = zl_db.Column(zl_db.String(50))  # 发布时间
    occ_href = zl_db.Column(zl_db.String(255))  # 职业链接
    com_href = zl_db.Column(zl_db.String(255))  # 公司链接
    status = zl_db.Column(zl_db.Integer, default=1)  # 状态


class City(zl_db.Model):
    __bind_key__ = 'zhilian'
    __tablename__ = 'city'
    id = zl_db.Column(zl_db.Integer, primary_key=True, autoincrement=True)
    city = zl_db.Column(zl_db.String(100), nullable=True, unique=True)  # 城市名
    code = zl_db.Column(zl_db.Integer, nullable=True, unique=True)  # 城市对应号码
    status = zl_db.Column(zl_db.Integer, default=1)  # 状态
