from app.controller.use_mysql import find_mysql, insert_mysql, insert_mysql_in_city
from app.spider import SPIDER


class HOME:

    def __init__(self, form):
        '''
        :param form: 客户端提交的数据  类型:dict
        '''
        self.form = form

    def home(self):
        web = self.form['web']
        key = self.form['key']
        city = self.form['city']

        # 城市表插入数据
        # print('城市及对应代码爬取中....')
        # result = SPIDER(web=web).get_city()
        # insert_mysql_in_city(web=web, result=result)
        # print('城市及对应代码爬取完毕!')

        # 数据库中查询数据
        data = find_mysql(web=web, job=key, city=city)
        if web != 'zhilian':
            page = SPIDER(web=web, key=key, city=city).get_page()
        for values in list(data.values()):
            print('数据库中数据数:', len(values))
            if len(values) <= 300 or len(values) <= (page - 1) * 50:
                print('%s爬取中.....' % web)
                data = SPIDER(web=web, key=key, city=city).get_data()
                # print('爬虫结果:', len(data), data)
                if list(data.values()):
                    insert_mysql(web=web, data=data)
                else:
                    raise NameError('查询到的数据为空。错误原因:1、输入的职位不正确\n2、城市不存在\n3、没有该招聘信息')
        return data
