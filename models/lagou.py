from flask_sqlalchemy import SQLAlchemy

lg_db = SQLAlchemy()


class Lagou(lg_db.Model):
    __bind_key__ = 'lagou'  # 数据库：lagou
    __tablename__ = 'data'
    id = lg_db.Column(lg_db.Integer, primary_key=True, autoincrement=True)
    key = lg_db.Column(lg_db.String(10))  # 搜索职业
    city = lg_db.Column(lg_db.String(10))  # 搜索城市
    occupation = lg_db.Column(lg_db.String(50))  # 职业
    company_name = lg_db.Column(lg_db.String(30))  # 公司名字
    address = lg_db.Column(lg_db.String(30))  # 地址
    salary = lg_db.Column(lg_db.String(30))  # 薪资
    release_time = lg_db.Column(lg_db.String(50))  # 发布时间
    occ_href = lg_db.Column(lg_db.String(255))  # 职业链接
    com_href = lg_db.Column(lg_db.String(255))  # 公司链接
    status = lg_db.Column(lg_db.Integer, default=1)  # 状态


class City(lg_db.Model):
    __bind_key__ = 'lagou'  # 数据库：lagou
    __tablename__ = 'city'
    id = lg_db.Column(lg_db.Integer, primary_key=True, autoincrement=True)
    city = lg_db.Column(lg_db.String(100), nullable=True, unique=True)  # 城市名
    code = lg_db.Column(lg_db.Integer, nullable=True, unique=True)  # 城市对应号码
    status = lg_db.Column(lg_db.Integer, default=1)  # 状态
