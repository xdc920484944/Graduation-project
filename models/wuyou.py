from flask_sqlalchemy import SQLAlchemy

wy_db = SQLAlchemy()


class Wuyou(wy_db.Model):  # 默认数据库
    __tablename__ = 'data'
    id = wy_db.Column(wy_db.Integer, primary_key=True, autoincrement=True)
    key = wy_db.Column(wy_db.String(10))  # 搜索职业
    city = wy_db.Column(wy_db.String(10))  # 搜索城市
    occupation = wy_db.Column(wy_db.String(50))  # 职业
    company_name = wy_db.Column(wy_db.String(30))  # 公司名字
    address = wy_db.Column(wy_db.String(30))  # 地址
    salary = wy_db.Column(wy_db.String(30))  # 薪资
    release_time = wy_db.Column(wy_db.String(50))  # 发布时间
    occ_href = wy_db.Column(wy_db.String(255))  # 职业链接
    com_href = wy_db.Column(wy_db.String(255))  # 公司链接
    status = wy_db.Column(wy_db.Integer, default=1)  # 状态


class City(wy_db.Model):
    __tablename__ = 'city'
    id = wy_db.Column(wy_db.Integer, primary_key=True, autoincrement=True)
    city = wy_db.Column(wy_db.String(100), nullable=True, unique=True)  # 城市名
    code = wy_db.Column(wy_db.Integer, nullable=True, unique=True)  # 城市对应号码
    status = wy_db.Column(wy_db.Integer, default=1)  # 状态
