from app.controller.use_mysql import find_mysql_in_city
from app.spider.lagou.main import get_data_lagou
from app.spider.tc.main import get_data_tc
from app.spider.wuyou.get_content import Get_content
from app.spider.wuyou.main import get_data_wuyou
from app.spider.zhilian.main import get_data_zhilian


class SPIDER:
    def __init__(self, web='', key='', city=''):
        '''
        爬虫入口
        数据格式:{查询的职业:[查询的城市, 详细职业名，公司名，地址，工资，时间，招聘URL，公司URL，城市CODE]}
        :param web:网站名
        :param key:职位
        :param city: 城市
        '''
        self.web = web
        self.key = key
        self.city = city

    def get_data(self):
        '''
        需要web、job、city
        :return:
        '''
        if self.web == '51job':
            data = get_data_wuyou(web=self.web, key=self.key, city=self.city)
        if self.web == 'tc':
            data = get_data_tc(web=self.web, key=self.key, city=self.city)
        return data

    def get_job_content(self, web, data):
        job_inf, com_inf = Get_content(web=web, data=data)
        return job_inf, com_inf

    def get_page(self):
        if self.web == '51job':
            from app.spider.wuyou.get_page import Get_page
            page = Get_page()
        elif self.web == 'tc':
            from app.spider.tc.get_page import Get_page
            from app.spider.tc.main import creat_driver
            driver = creat_driver()
            code = find_mysql_in_city(web=self.web, city=self.city)
            url = 'https://{}.58.com/job/pn{}/?key={}&classpolicy=job_A&final=1&jump=1'.format(code, 1, self.key)
            driver.get(url=url)
            page = Get_page(driver)
            driver.close()
        return page

    def get_city(self):
        if self.web == '51job':
            pass
        elif self.web == 'tc':
            from app.spider.tc.get_city import Get_city
            return Get_city()


if __name__ == "__main__":
    a = SPIDER(web='tc').get_city()
    print(a)
