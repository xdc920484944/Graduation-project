from app.spider.fram import close_fram
import datetime
from app.spider.scroll_down import scroll_down
from app.spider.zhilian.get_page import get_page

# ！/usr/bin/env python
# -*-coding:utf-8-*-
"""
@Author  : xiaofeng
@Time    : 2018/12/18 16:31
@Desc : Less interests,More interest. (爬取智联招聘职位数据)
@Project : python_appliction
@FileName: zhilianzhaopin.py
@Software: PyCharm
@Blog    ：https://blog.csdn.net/zwx19921215
"""
import json

import pymysql as db
import requests

# mysql配置信息
mysql_config = {
    'host': '101.0.2.110',
    'user': 'test',
    'password': 'test',
    'database': 'xiaofeng',
    'charset': 'utf8'
}

# url
url = 'https://data.highpin.cn/api/JobSearch/Search'

"""
爬取智联招聘职位数据
@:param page 页码
@:param position 职位关键字
"""


def zhilian(page, position):
    # 封装头信息
    headers = {
        'Referer': 'https://www.highpin.cn/zhiwei/',
        'Origin': 'https://www.highpin.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'application/json, text/javascript, * / *; q=0.01',
    }
    # 表单信息
    datas = {
        'Q': position,
        'pageIndex': page
    }
    resp = requests.post(url, data=datas, headers=headers)
    result = resp.json()
    return result


def Get_imformation(key):
    '''
    获取智联招聘详细信息
    :param position:
    :return: {'搜索职位':[职位名,公司名,地址,学历要求,工作经验,所在行业,发布时间,公司规模,],[]}
    '''
    data = {key: []}
    result = zhilian(1, key)
    page_count = result['body']['PageCount']
    page = 1
    while page <= page_count:
        result = zhilian(page, key)
        body = result['body']['JobList']
        for b in body:
            data[key].append([
                b['JobTitle'], b['CompanyName'], b['JobLactionStr'], b['JobDegree'], b['WorkExperience'],
                b['CompanyIndustry'], b['CompanyType'], b['PublishDate'], b['CompanyScale']])
        page += 1
    return data


if __name__ == '__main__':
    data = Get_imformation('python')

# def Get_imfomation(driver):
#     data = {}
#     occ_hrefs = driver.find_elements_by_xpath(
#         '//*[@id="listContent"]//div[@class="contentpile__content__wrapper__item clearfix"]/a')  # get
#     job_names = driver.find_elements_by_xpath(
#         '//*[@id="listContent"]//div[@class="contentpile__content__wrapper__item__info__box__jobname jobName"]')  # T
#     com_names = driver.find_elements_by_xpath(
#         '//div[@class="contentpile__content__wrapper__item clearfix"]/a/div[1]/div[2]/a')  # T
#     com_hrefs = []
#     for c in com_names:
#         com_hrefs.append(c.get_attribute('href'))
#
#     print(len(occ_hrefs), len(job_names), len(com_names), len(com_hrefs))
#     return data
#
#
# if __name__ == '__main__':
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     page = 1
#     key = 'python'
#     code = '530'  # 北京
#     url = 'https://sou.zhaopin.com/?p={}&jl={}&kw={}&kt=3'.format(page, code, key)
#     print(url)
#     driver.get(url)
#     Get_imfomation(driver)
