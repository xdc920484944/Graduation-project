from flask_sqlalchemy import SQLAlchemy

tc_db = SQLAlchemy()


# 数据格式：{搜索关键字:[职位, 公司名, 薪资, 发布时间, 职位链接, 公司链接, 福利, 要求, 城市], []}
class Tc(tc_db.Model):  # 默认数据库,保存所有招聘信息
    __bind_key__ = 'tc'  # 数据库：tc
    __tablename__ = 'data'
    id = tc_db.Column(tc_db.Integer, primary_key=True, autoincrement=True)
    key = tc_db.Column(tc_db.String(10))  # 搜索职业
    city = tc_db.Column(tc_db.String(10))  # 搜索城市
    occupation = tc_db.Column(tc_db.String(50))  # 职业
    company_name = tc_db.Column(tc_db.String(30))  # 公司名字
    # address = tc_db.Column(tc_db.String(30))  # 地址
    salary = tc_db.Column(tc_db.String(30))  # 薪资
    release_time = tc_db.Column(tc_db.String(50))  # 发布时间
    occ_href = tc_db.Column(tc_db.Text)  # 职业链接
    com_href = tc_db.Column(tc_db.Text)  # 公司链接
    welfare = tc_db.Column(tc_db.String(100))  # 福利
    require = tc_db.Column(tc_db.String(50))  # 要求
    status = tc_db.Column(tc_db.Integer, default=1)  # 状态


class Job(tc_db.Model):  # 保存职位详细信息
    __bind_key__ = 'tc'  # 数据库：tc
    __tablename__ = 'job'
    id = tc_db.Column(tc_db.Integer, primary_key=True, autoincrement=True)
    url = tc_db.Column(tc_db.String(255), unique=True)  # 网址
    request = tc_db.Column(tc_db.Text)  # 职位需求
    welfare = tc_db.Column(tc_db.Text)  # 福利
    content = tc_db.Column(tc_db.Text)  # 职位详细信息
    creat_time = tc_db.Column(tc_db.String(50))  # 创建时间
    status = tc_db.Column(tc_db.Integer, default=1)  # 状态


class City(tc_db.Model):
    __bind_key__ = 'tc'  # 数据库：tc
    __tablename__ = 'city'
    id = tc_db.Column(tc_db.Integer, primary_key=True, autoincrement=True)
    city = tc_db.Column(tc_db.String(100), nullable=True, unique=True)  # 城市名
    href = tc_db.Column(tc_db.String(255), nullable=True, unique=True)  # url
    code = tc_db.Column(tc_db.String(20), nullable=True, unique=True)  # 城市对应号码
    status = tc_db.Column(tc_db.Integer, default=1)  # 状态
