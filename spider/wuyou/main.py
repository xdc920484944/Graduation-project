from app.controller.use_mysql import find_mysql_in_city
from app.spider.wuyou.get_imformation import Get_imformation
from app.spider.wuyou.get_page import Get_page


def get_data_wuyou(web, key, city):
    '''
    爬取无忧网数据
    :param web: 网站
    :param key: 职位
    :param city: 城市
    :return:    dict 数据格式:{职业:[[职业名，公司名，地址，工资，发布时间，职位URL，公司URL，城市],[],.....]}
    '''
    code = find_mysql_in_city(web=web, city=city)
    if code == [] or code == '':
        raise NameError('城市编号为空。错误原因:1、城市不存在\n2、数据库中无数据')
    url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html?'.format(code, key)
    page = Get_page(url)
    try:
        data = {}
        data[key] = []
        for i in range(page):
            url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?'.format(code, key, i + 1)
            for k in Get_imformation(url):
                k.append(city)
                data[key].append(k)
        return data
    except:
        print('数据爬取出错:', url)


if __name__ == '__main__':
    job = '司机'
    city_code = '010000'
    city = '北京'
    data = get_data_wuyou(job=job, city_code=city_code, city=city)
    print(data)
