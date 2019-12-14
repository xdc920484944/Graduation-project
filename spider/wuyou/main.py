from pprint import pprint

from app.setting import MAX_PAGE
from app.spider.wuyou.get_imformation import Get_imformation
from app.spider.wuyou.get_page import Get_page


def get_data_wuyou(occupation, city, city_code=''):
    '''
    爬取无忧网数据
    :param occupation: 职位
    :param city: 城市
    :param city_code:城市代码
    :return:
    '''
    url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html?'.format(city_code, occupation, )
    page = Get_page(url)
    data = {}
    data[occupation] = []
    for i in range(page):
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?'.format(city_code, occupation, i + 1)
        for k in Get_imformation(url):
            k.append(city)
            data[occupation].append(k)
    return data


# 数据格式:{查询的职业:[查询的城市, 详细职业名，公司名，地址，工资，时间，招聘URL，公司URL，城市CODE]}
if __name__ == '__main__':
    occupation = '司机'
    city_code = '010000'
    city = '北京'
    data = get_data_wuyou(occupation=occupation, city_code=city_code, city=city)
    print(data)
