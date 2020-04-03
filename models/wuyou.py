from flask_sqlalchemy import SQLAlchemy

wy_db = SQLAlchemy()


class Wuyou(wy_db.Model):  # 默认数据库,保存所有招聘信息
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


class Job(wy_db.Model):  # 保存职位详细信息
    __tablename__ = 'job'
    id = wy_db.Column(wy_db.Integer, primary_key=True, autoincrement=True)
    url = wy_db.Column(wy_db.String(255))  # 网址
    request = wy_db.Column(wy_db.Text)  # 职位需求
    welfare = wy_db.Column(wy_db.Text)  # 福利
    content = wy_db.Column(wy_db.Text)  # 职位详细信息
    creat_time = wy_db.Column(wy_db.String(50))  # 创建时间
    status = wy_db.Column(wy_db.Integer, default=1)  # 状态


class Company(wy_db.Model):
    __tablename__ = 'company'
    id = wy_db.Column(wy_db.Integer, primary_key=True, autoincrement=True)
    url = wy_db.Column(wy_db.String(255))  # 职业
    content = wy_db.Column(wy_db.Text)  # 公司详细信息
    type = wy_db.Column(wy_db.String(50))  # 公司类型
    size = wy_db.Column(wy_db.String(100))  # 公司规模
    work_in = wy_db.Column(wy_db.Text)  # 公司业务方向
    creat_time = wy_db.Column(wy_db.String(50))  # 创建时间
    status = wy_db.Column(wy_db.Integer, default=1)  # 状态


class City(wy_db.Model):
    __tablename__ = 'city'
    id = wy_db.Column(wy_db.Integer, primary_key=True, autoincrement=True)
    city = wy_db.Column(wy_db.String(100), nullable=True, unique=True)  # 城市名
    code = wy_db.Column(wy_db.String(20), nullable=True, unique=True)  # 城市对应号码
    status = wy_db.Column(wy_db.Integer, default=1)  # 状态
