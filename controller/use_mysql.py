# 无忧数据库操作
import time

from app.models.lagou import Lagou, lg_db
from app.models.wuyou import Wuyou, City, wy_db
from app.models.zhilian import Zhilian, zl_db
from app.spider.wuyou.get_city import Get_city

# 数据格式：{搜索关键字:[职位，公司名字，地点，薪资，发布时间，职位链接，公司链接, 城市], [...]}
# data数据插入
def insert_mysql(data, web):

    for k, v in data.items():
        for i in v:
            if web == '51job':
                params = Wuyou(key=k, city=i[7], occupation=i[0], company_name=i[1], address=i[2], salary=i[3],
                               release_time=i[4],
                               occ_href=i[5], com_href=i[6])
                wy_db.session.add(params)
                wy_db.session.commit()
            if web == 'lagou':
                params = Lagou(key=k, city=i[7], occupation=i[0], company_name=i[1], address=i[2], salary=i[3],
                               release_time=i[4],
                               occ_href=i[5], com_href=i[6])
                lg_db.session.add(params)
                lg_db.session.commit()
            if web == 'zhilian':
                params = Zhilian(key=k, city=i[7], occupation=i[0], company_name=i[1], address=i[2], salary=i[3],
                                 release_time=i[4],
                                 occ_href=i[5], com_href=i[6])
                zl_db.session.add(params)
                zl_db.session.commit()
    print('数据插入完成！')
    return data


# data数据查找
def find_mysql(web, occupation, city):
    result = []
    if web == '51job':
        result = Wuyou.query.filter(Wuyou.key == occupation, Wuyou.city == city).all()
    if web == 'lagou':
        result = Lagou.query.filter(Lagou.key == occupation, Lagou.city == city).all()
    if web == 'zhilian':
        result = Zhilian.query.filter(Zhilian.key == occupation, Zhilian.city == city).all()

    # if len(result) == 0:
    #     print('数据库中找不到数据！')
    #     return []
    # else:
    #     print('数据库中找到了数据！')
    return result


# city表数据插入
def insert_mysql_in_city():
    citys = Get_city()  # 数据插入
    print(citys)
    for k, v in citys.items():
        params = City(city=k, code=v)
        wy_db.session.add(params)
        wy_db.session.commit()
    print('city表数据插入完成!')


# city表数据查询
def find_mysql_in_city(city=''):
    '''
    传入城市名，在数据库中查询所对应的编号
    :param city: 类型->str 城市名
    :return:
    '''
    result = City.query.filter(City.city == city).first()
    if result == None:
        return result
    else:
        return result.code


# key大于15->数据库中的status置零
def split_release_time(release_time='2019-09-24'):
    release_time = release_time.split('-')
    now = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')
    lis = []
    for i in range(3):
        lis.append(int(now[i]) - int(release_time[i]))
    day = lis[0] * 365 + lis[1] * 30 + lis[2]
    if day < 15:
        key = 1
    else:
        key = 0
    return key


if __name__ == '__main__':
    data = {'北京':['java开发工程师4', '深圳神木源科技有限公司', '深圳-南山区', '6-8千/月', '2019-11-17', 'https://jobs.51job.com/shenzhen-nsq/116491956.html?s=01&t=0', 'https://jobs.51job.com/all/co5616198.html', '北京']}
    # find_mysql_in_city()
    insert_mysql(data=data,web='wuyou')