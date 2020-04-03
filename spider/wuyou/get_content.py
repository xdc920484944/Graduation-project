import random

import requests
from lxml import etree

from app.controller.use_mysql import insert_mysql_in_job, find_mysql_in_job, find_mysql_in_company, \
    insert_mysql_in_company, alter_mysql
from app.setting import MAX_LINE


def Get_content(web, data):
    '''
    获取职位和公司详细信息
    :param data:源数据
    :return: dict,dict
             job_information={url1:[request, welfare, content], url2:[]......}
             company_information={url1:[url, content, type, size, work_in], url2:[].....}
    '''

    def get_urls():
        '''
        获取所有职位信息的url
        :param data:
        :return: [url1,url2,...]
        '''
        w_f_value = list(data.values())[0]
        num = MAX_LINE if len(w_f_value) > MAX_LINE else len(w_f_value)
        job_url_list = []
        com_url_list = []
        for values in random.sample(w_f_value, num):
            job_url = values[5]
            com_url = values[6]
            job_url_list.append(job_url)
            com_url_list.append(com_url)
        return job_url_list, com_url_list

    # 数据库查询
    job_url_list, com_url_list = get_urls()  # 获取源数据中 MAX_LINE 条职位的url
    job_inf_mysql, job_url_list = find_mysql_in_job(web=web, url_list=job_url_list)  # 数据库中职位的详细数据（返回的是个对象）
    com_inf_mysql, com_url_list = find_mysql_in_company(web=web, url_list=com_url_list)  # 数据库中公司的详细数据 （返回的是个对象）
    job_information = {}
    company_information = {}
    print(job_inf_mysql, com_inf_mysql)

    # 爬虫
    if job_url_list:
        print('职位信息需要爬取数:', len(job_url_list))
        old_data = []
        for job_url in job_url_list:
            res = requests.get(job_url)
            if res.status_code == 404:  # 招聘信息不存在时，服务器返回状态码为404
                old_data.append(job_url)
                continue
            else:
                res.encoding = res.apparent_encoding
                html = etree.HTML(res.content)
                try:
                    job_request = html.xpath('/html/body//p[@class="msg ltype"]/@title')[0].replace('\xa0', '')  # 职位要求
                    job_welfare = ';'.join(html.xpath('/html/body//div[@class="jtag"]//span/text()'))  # 福利
                    job_content = ''.join(html.xpath('/html/body//div[@class="bmsg job_msg inbox"]//text()')
                                          ).replace('\r\n', '').replace(' ', '')  # 职位描述

                    com_url = html.xpath('/html/body//div[@class="com_msg"]/a/@href')[0]  # 公司url
                    com_content = html.xpath('/html/body//div[@class="tmsg inbox"]/text()')[0]  # 公司描述
                    com_type = html.xpath('/html/body//div[@class="com_tag"]/p[1]/@title')[0]  # 公司资本类型
                    com_size = html.xpath('/html/body//div[@class="com_tag"]/p[2]/@title')[0]  # 公司规模
                    com_work_in = html.xpath('/html/body//div[@class="com_tag"]/p[3]/@title')[0]  # 公司类型
                except:
                    print('职位、公司详情获取失败:', job_url)
                    continue
                job_information[job_url] = [job_request, job_welfare, job_content]
                company_information[com_url] = [com_content, com_type, com_size, com_work_in]
        # 数据插入
        if job_information or company_information:
            insert_mysql_in_job(web=web, data=job_information)
            insert_mysql_in_company(web=web, data=company_information)

        # 数据更新
        alter_mysql(web=web, occ_list=old_data)

    for obj in job_inf_mysql:  # 将数据库中查找到的对象转换为可用数据格式，并存入job_information中
        job_information[obj.url] = [obj.request, obj.welfare, obj.content]

    for obj in com_inf_mysql:  # 将数据库中查找到的对象转换为可用数据格式，并存入com_information中
        company_information[obj.url] = [obj.content, obj.type, obj.size, obj.work_in]

    return job_information, company_information


if __name__ == '__main__':
    data = {'.net': [['.NET开发工程师', '“前程无忧”51job.com（上海）', '上海-浦东新区', None, '2020-02-13',
                      'http://51job.com/sc/show_job_detail.php?jobid=103391010',
                      'https://jobs.51job.com/all/co1249.html', '上海'],
                     ['.NET架构师', '精锐教育', '上海-普陀区', '2.5-3万/月', '2020-02-21',
                      'https://jobs.51job.com/shanghai-ptq/120088980.html?s=01&t=0',
                      'https://jobs.51job.com/all/co2108291.html', '上海']]}
    job_information, company_information = Get_content(data)
    print(job_information)
    print(company_information)
