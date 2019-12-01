from app.models.lagou import Lagou
from app.models.wuyou import Wuyou
from app.models.zhilian import Zhilian

def get_form(Form):
    form = Form

#通过模型调用数据库
class Mysql:
    def __init__(self, db, occupation, city):
        self.query_result = ''
        self.db = db
        self.occupation = occupation
        self.city = city

    # 数据查询
    def query_mysql(self):
        if self.db == 'wuyou':
            self.query_result = Wuyou.query.all()
        if self.db == 'lagou':
            self.query_result = Lagou.query.all()
        if self.db == 'zhilian':
            self.query_result = Zhilian.query.all()

    # 数据插入
    def insert_mysql(self):
        pass


    # def query_wuyou_mysql(self):
    #     result = Wuyou.query.all()
    #     self.query_result = result
    #
    # def query_lagou_mysql(self):
    #     pass
    #
    # def query_zhilian_mysql(self):
    #     pass
