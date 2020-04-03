import re
from selenium import webdriver

from app.spider.tc.main import creat_driver


def Get_city():
    '''
    获取58同城可搜索城市及对应网站
    :param url:
    :return: {city_name:[href, code], city_name:[href, code], ...}
    '''
    url = 'https://www.58.com/changecity.html?catepath=job&catename=%E5%85%A8%E8%81%8C%E6%8B%9B%E8%81%98&fullpath=9224&PGTID=0d302408-0000-24a8-5688-4ee40ffe71dd&ClickID=2'
    driver = creat_driver()
    driver.get(url)
    citys = driver.find_elements_by_xpath('//*[@id="content-box"]//div[@class="content-cities"]/a')
    print('citys长度:', len(citys))
    result = {}
    for city in citys:
        href = city.get_attribute('href')
        code = re.findall('//(\w*).', href)[0]
        name = city.text
        result[name] = [href, code]
    return result

