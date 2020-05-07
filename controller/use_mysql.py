# 无忧数据库操作
import time

from app.models import tc_db, zl_db
from app.models.tc import Tc
from app.models.wuyou import Wuyou, wy_db, Company

# 51数据格式：{搜索关键字:[职位，公司名字，地点，薪资，发布时间，职位链接，公司链接, 城市], [...]}
# tc数据格式：{搜索关键字:[[职位名(0),公司名(1),薪资(2),发布时间(3),职位链接(4),公司链接(5),福利(6),要求(7),城市(8)], [],...]}
# zl数据格式: {'搜索职位':[[职位名0,公司名1,地址2,学历要求3,工作经验4,所在行业5,发布时间6,公司规模7,],[]]}
# data表-插入
from app.models.zhilian import Zhilian


def insert_mysql(web, data):
    for k, v in data.items():
        for i in v:
            try:
                if web == '51job':
                    params = Wuyou(key=k, city=i[7], occupation=i[0], company_name=i[1], address=i[2], salary=i[3],
                                   release_time=i[4],
                                   occ_href=i[5], com_href=i[6])
                    wy_db.session.add(params)
                    wy_db.session.commit()
                if web == 'tc':
                    params = Tc(key=k, city=i[8], occupation=i[0], company_name=i[1], salary=i[2], release_time=i[3],
                                occ_href=i[4], com_href=i[5], welfare=i[6], require=i[7])
                    wy_db.session.add(params)
                    wy_db.session.commit()
                if web == 'zhilian':
                    params = Zhilian(key=k, occupation=i[0], company_name=i[1], address=i[2], job_degree=i[3],
                                     epx=i[4], industry=i[5], release_time=i[6], com_model=i[7])
                    zl_db.session.add(params)
                    zl_db.session.commit()
            except Exception as e:
                print('数据库数据插入错误:', i, e)

    print('data表数据插入完成！')
    # return data


# data表-查找
def find_mysql(web, job, city):
    # {职业:[[职业名，公司名，地址，工资，发布时间，职位URL，公司URL，城市],[...],]}
    result = {}
    if web == '51job':
        result[job] = Wuyou.query.filter(Wuyou.key == job, Wuyou.city == city, Wuyou.status == 1).all()
    elif web == 'tc':
        result[job] = Tc.query.filter(Tc.key == job, Tc.city == city, Tc.status == 1).all()
    elif web == 'zhilian':
        result[job] = Zhilian.query.filter(Zhilian.key == job, Zhilian.status == 1).all()
    r_to_d = result_to_data(web=web, result=result)  # 将数据库中查到的数据转换为字典格式
    data, old_data = Filter_Data.filter_time(web=web, data=r_to_d)  # 过滤超过期限数据
    if len(old_data[job]) > 0:
        # print('old_data:', old_data)
        occ_list = [x[5] for x in list(old_data.values())[0]]
        alter_mysql(web=web, occ_list=occ_list)
    return data


# data表-修改（软删除）
def alter_mysql(web, occ_list):
    if web == '51job':
        for url in occ_list:
            param = Wuyou.query.filter(Wuyou.occ_href == url, Wuyou.status == 1).first()
            param.status = -1
            wy_db.session.commit()
    print('data表删除的过期数据数量为:', len(occ_list))


# 职位表插入
def insert_mysql_in_job(web, data):
    '''
    :param web:
    :param data: job_information[job_url] = [job_request, job_welfare, job_content]
    :return:
    '''
    for k in data:
        if web == '51job':
            from app.models.wuyou import Job
            params = Job(url=k, request=data[k][0], welfare=data[k][1], content=data[k][2])
            wy_db.session.add(params)
            wy_db.session.commit()
    print('job表数据插入完成！')


# 职位表查询
def find_mysql_in_job(web, url_list):
    '''
    查询数据库中是否存在与url对应的数据
    :param web: 网站
    :param url_list:url列表 [url1, url2,....]
    :return:
    '''
    result = []
    if web == '51job':
        from app.models.wuyou import Job
        urls = []
        result = []
        for url in url_list:
            res = (Job.query.filter(Job.url == url, Job.status == 1).first())
            if res:
                result.append(res)
            else:
                urls.append(url)
    if web == 'tc':
        from app.models.tc import Job
        urls = []
        result = []
        for url in url_list:
            res = (Job.query.filter(Job.url == url, Job.status == 1).first())
            if res:
                result.append(res)
            else:
                urls.append(url)
    return result, urls


# 职位表修改
def alter_mysql_in_job(web, url_list):
    if web == '51job':
        for url in url_list:
            pass


# 公司表插入
def insert_mysql_in_company(web, data):
    '''
    将职位信息插入数据库中的position表中
    :param web:str eg:'51job'
    :param data: company_information[com_url] = [com_content, com_type, com_size, com_work_in]
    :return:
    '''
    for k in data:
        if web == '51job':
            params = Company(url=k, content=data[k][0], type=data[k][1], size=data[k][2], work_in=data[k][3])
            wy_db.session.add(params)
            wy_db.session.commit()

    print('company表数据插入完成！')


# 公司表查询
def find_mysql_in_company(web, url_list):
    '''
    查询数据库中是否存在与url对应的数据
    :param web: 网站
    :param url_list:url列表 [url1, url2,....]
    :return:
    '''
    result = []
    if web == '51job':
        urls = []
        result = []
        for url in url_list:
            res = (Company.query.filter(Company.url == url, Company.status == 1).first())
            if res:
                result.append(res)
            else:
                urls.append(url)

    return result, urls


# city表数据插入
def insert_mysql_in_city(web, result):
    if web == '51job':
        from app.models.wuyou import City
        for k, v in result.items():
            params = City(city=k, code=v)
            wy_db.session.add(params)
            wy_db.session.commit()
    if web == 'tc':
        from app.models.tc import City
        for k, v in result.items():
            params = City(city=k, href=v[0], code=v[1])
            tc_db.session.add(params)
            tc_db.session.commit()
    if web == 'zhilian':
        from app.models.zhilian import City
        for k, v in result.items():
            params = City(city=k, href=v[0], code=v[1])
            zl_db.session.add(params)
            zl_db.session.commit()
    print('city表数据插入完成!')


# city表数据查询
def find_mysql_in_city(web, city):
    '''
    传入城市名，在数据库中查询所对应的编号
    :param city: 类型->str 城市名
    :return:
    '''
    if web == '51job':
        from app.models.wuyou import City
        result = City.query.filter(City.city == city).first()
        result = result.code if result else ''

    elif web == 'tc':
        from app.models.tc import City
        result = City.query.filter(City.city == city).first()
        result = result.code if result else ''

    return result


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


# mysql数据转换为字典data
def result_to_data(web, result):
    '''
    :param result:查询mysql返回的数据
    :return: 源数据 data
    '''
    if web == '51job':
        for key, values in result.items():
            data = {key: []}
            for v in values:
                data[key].append([v.occupation, v.company_name, v.address, v.salary,
                                  v.release_time, v.occ_href, v.com_href, v.city])
    elif web == 'tc':
        for key, values in result.items():
            data = {key: []}
            for v in values:
                data[key].append(
                    [v.occupation, v.company_name, v.salary, v.release_time, v.occ_href, v.com_href, v.welfare,
                     v.require,
                     v.city])
    elif web == 'zhilian':
        for key, values in result.items():
            data = {key: []}
            for v in values:
                data[key].append(
                    [v.occupation, v.company_name, v.address, v.epx, v.industry, v.release_time, v.com_model, v.city])

    return data


# 时间检查
class Filter_Data:
    @classmethod
    def filter_time(cls, web, data):
        '''
        过滤过期数据
        :param data: 源数据
        :return: new_data(未过期数据):{job:[[],[],]}   old_data(过期数据)：{job:[[],[],]}
        t2 = time.strftime("%Y-%m-%d", time.localtime(t1)) stamp -> date
        t3 = time.mktime(time.strptime(t1, '%Y-%m-%d')) - time.mktime(time.strptime(t2, '%Y-%m-%d'))  # data -> stamp
        一个月差的时间戳2505600
        '''
        for job, values in data.items():
            new_data = {job: []}
            old_data = {job: []}
            if web == '51job':
                for v in values:
                    t1 = v[4].split('-')
                    t2 = time.strftime('%Y-%m-%d', time.localtime()).split('-')
                    k = (int(t2[0]) - int(t1[0])) * 365 + (
                            int(t2[1]) - int(t1[1])) * 30 + (
                                int(t2[2]) - int(t1[2]))
                    if k < 15:
                        new_data[job].append(v)
                    else:
                        old_data[job].append(v)
            if web == 'tc':
                new_data = data
        return new_data, old_data


if __name__ == '__main__':
    data = {'北京': ['java开发工程师4', '深圳神木源科技有限公司', '深圳-南山区', '6-8千/月', '2019-11-17',
                   'https://jobs.51job.com/shenzhen-nsq/116491956.html?s=01&t=0',
                   'https://jobs.51job.com/all/co5616198.html', '北京']}
    # find_mysql_in_city()
    # insert_mysql(data=data, web='wuyou')
