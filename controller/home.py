from app import spider
from app.analyze.easy_analyze import Easy_Analyze
from app.controller.use_mysql import find_mysql_in_city, find_mysql, insert_mysql
from app.models.lagou import Lagou
from app.models.wuyou import Wuyou
from app.models.zhilian import Zhilian
from app.spider.lagou.main import get_data_lagou
from app.spider.wuyou.main import get_data_wuyou
from app.spider.zhilian.main import get_data_zhilian


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
        result = Easy_Analyze(result).result  # 数据分析
        print('分析结果:', result)
        return result

        # if web == '51job':
        #     # 数据库查询
        #     data = find_mysql(web=web, occupation=occupation, city=city)
        #     if data != []:
        #         print('数据库中存在数据....')
        #         result = {occupation: []}
        #         # 整理数据格式
        #         for d in range(len(data)):
        #             result[occupation].append([data[d].occupation, data[d].company_name,
        #                                        data[d].address, data[d].salary, data[d].release_time, data[d].occ_href,
        #                                        data[d].com_href, data[d].city])
        #     # 数据库中查询不到数据则爬取数据
        #     else:
        #         print('无忧网爬取中.....')
        #         data = spider.SPIDER(web=web, occupation=occupation, city=city).data
        #         if len(data) != 0:
        #             insert_mysql(web=web, data=data)
        #         else:
        #             raise NameError('查询到的数据为空。错误原因:1、输入的职位不正确\n2、城市不存在\n3、没有该招聘信息')
        #         print('源数据:', data)
        #         result = data
        #
        #
        #     result = Easy_Analyze(result).result  # 数据分析
        #     print('分析结果:', result)
        #     return result
