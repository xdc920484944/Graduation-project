DEBUG = True

SQLALCHEMY_BINDS = {  # 多数据库导入
    'lagou': 'mysql+cymysql://root:@localhost/lagou',
    'zhilian': 'mysql+cymysql://root:@localhost/zhilian',
    'user': 'mysql+cymysql://root:@localhost/user',
    'tc': 'mysql+cymysql://root:@localhost/tc',
    'test': 'mysql+cymysql://root:@localhost/test'
}
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:@localhost/51job?charset=utf8'  # 默认数据库引擎
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '123456'
