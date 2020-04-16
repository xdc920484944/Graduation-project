import json
import re

import requests
from selenium import webdriver


def Get_city():
    '''
    获取智联招聘城市及对应代码
    :return: {city_name:[url,code], city_name:[],...}
    '''
    driver = webdriver.Chrome()
    key = 'python'
    code = '530'  # 北京
    url = 'https://sou.zhaopin.com/?jl={}&kw={}&kt=3'.format(code, key)
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
    driver.find_element_by_xpath('//*[@id="queryTitleUls"]/li[1]').click()
    citys = driver.find_elements_by_xpath(
        '//*[@id="queryCityBox"]/div/ul/li')
    codes = driver.find_elements_by_xpath('//*[@id="queryCityBox"]/div/ul/li/a')
    result = {}
    for n in range(len(citys)):
        code = re.findall('https://sou.zhaopin.com/\?jl=(\d*)', codes[n].get_attribute('href'))[0]
        url = codes[n].get_attribute('href').replace('&kw=python', '')
        result[citys[n].text] = ([url, code])
    driver.close()
    return result


def get_citycode(city):
    '''
    获取城市对应代码
    :param city:
    :return:
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Origin": "https://sou.zhaopin.com",
        "Host": "fe-api.zhaopin.com",
        "Accept-Encoding": "gzip, deflate, br"
    }
    url = "https://fe-api.zhaopin.com/c/i/city-page/user-city?ipCity={}".format(city)
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    return result['data']['code']

if __name__ == '__main__':
    Get_city()
