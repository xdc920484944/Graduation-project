from app import spider
from app.controller.use_mysql import find_mysql_in_city, find_mysql, insert_mysql



class HOME:

    def __init__(self, form):
        '''
        :param form: 客户端提交的数据  类型:dict
        '''
        self.form = form

    def home(self):
        web = self.form['web']
        occupation = self.form['job']
        city = self.form['city']

        # 数据库中查询数据
        data = find_mysql(web=web, occupation=occupation, city=city)
        if data != []:
            print('数据库中存在数据....')
            result = {occupation: []}
            # 整理数据格式
            for d in range(len(data)):
                result[occupation].append([data[d].occupation, data[d].company_name,
                                           data[d].address, data[d].salary, data[d].release_time, data[d].occ_href,
                                           data[d].com_href, data[d].city])
        else:
            print('%s爬取中.....' % web)
            data = spider.SPIDER(web=web, occupation=occupation, city=city).data
            if len(data) != 0:
                insert_mysql(web=web, data=data)
                result = data
            else:
                raise NameError('查询到的数据为空。错误原因:1、输入的职位不正确\n2、城市不存在\n3、没有该招聘信息')
        print('源数据:', result)
        return result