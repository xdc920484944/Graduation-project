from selenium import webdriver
from app.controller.use_mysql import find_mysql_in_city
from app.spider.tc.get_imformation import Get_imformation
from app.spider.tc.get_page import Get_page


def creat_driver():
    '''
    谷歌浏览器实例化
    :return:
    '''
    chrome_opt = webdriver.ChromeOptions()

    # 无图浏览
    prefs = {'profile.managed_default_content_settings.images': 2}
    chrome_opt.add_experimental_option('prefs', prefs)
    # 无头模式
    chrome_opt.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_opt)
    return driver


# 数据格式：{搜索关键字:[[职位名,公司名,薪资,发布时间,职位链接,公司链接,福利,要求,城市], [],...]}
def get_data_tc(web, key, city):
    driver = creat_driver()
    code = find_mysql_in_city(web=web, city=city)
    # code = 'bj'
    or_url = 'https://{}.58.com/job/pn{}/?key={}&classpolicy=job_A&final=1&jump=1'
    url = or_url.format(code, 1, key)
    driver.get(url)
    pages = Get_page(driver)
    data = {key: []}
    for page in range(pages):
        if page > 0:
            url = or_url.format(code, page + 1, key)
            driver.get(url)
        one_page = Get_imformation(driver=driver)
        for r in one_page:
            r.append(city)
            data[key].append(r)
    driver.close()
    return data


if __name__ == '__main__':
    get_data_tc(web='tc', city='北京', key='司机')
