from flask_sqlalchemy import SQLAlchemy

zl_db = SQLAlchemy()


# {'搜索职位':[职位名,公司名,地址,学历要求,工作经验,所在行业,发布时间,公司规模,],[]}
class Zhilian(zl_db.Model):
    __bind_key__ = 'zhilian'
    __tablename__ = 'data'
    id = zl_db.Column(zl_db.Integer, primary_key=True, autoincrement=True)
    key = zl_db.Column(zl_db.String(10))  # 搜索职业
    occupation = zl_db.Column(zl_db.String(50))  # 职业
    company_name = zl_db.Column(zl_db.String(30))  # 公司名字
    address = zl_db.Column(zl_db.String(30))  # 地址
    job_degree = zl_db.Column(zl_db.String(30))  # 学历要求
    epx = zl_db.Column(zl_db.String(30))  # 工作经验
    industry = zl_db.Column(zl_db.String(90))  # 所在行业
    release_time = zl_db.Column(zl_db.String(50))  # 发布时间
    com_model = zl_db.Column(zl_db.String(30))  # 公司规模
    status = zl_db.Column(zl_db.Integer, default=1)  # 状态
    # city = zl_db.Column(zl_db.String(10))  # 搜索城市
    # salary = zl_db.Column(zl_db.String(30))  # 薪资
    # occ_href = zl_db.Column(zl_db.String(255))  # 职业链接
    # com_href = zl_db.Column(zl_db.String(255))  # 公司链接


class City(zl_db.Model):
    __bind_key__ = 'zhilian'
    __tablename__ = 'city'
    id = zl_db.Column(zl_db.Integer, primary_key=True, autoincrement=True)
    city = zl_db.Column(zl_db.String(100), nullable=True, unique=True)  # 城市名
    code = zl_db.Column(zl_db.Integer, nullable=True, unique=True)  # 城市对应号码
    href = zl_db.Column(zl_db.Text)
    status = zl_db.Column(zl_db.Integer, default=1)  # 状态
