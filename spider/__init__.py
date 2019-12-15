from app.controller.use_mysql import find_mysql_in_city
from app.spider.lagou.main import get_data_lagou
from app.spider.wuyou.main import get_data_wuyou
from app.spider.zhilian.main import get_data_zhilian


class SPIDER:
    def __init__(self, web, occupation, city):
        '''
        爬虫入口
        数据格式:{查询的职业:[查询的城市, 详细职业名，公司名，地址，工资，时间，招聘URL，公司URL，城市CODE]}
        :param web:网站名
        :param occupation:职位
        :param city: 城市
        '''
        if web == '51job':
            city_code = find_mysql_in_city(city)
            if city_code == [] or city_code == '':
                raise NameError('城市编号为空。错误原因:1、城市不存在\n2、数据库中无数据')
            self.data = get_data_wuyou(occupation=occupation, city=city, city_code=city_code)
        elif web == 'zhilian':
            self.data = get_data_zhilian(occupation=occupation, city=city)
        elif web == 'lagou':
            self.data = get_data_lagou(occupation=occupation, city=city)
        else:
            raise NameError('该网站还未加入加入，请换个网站试试')
