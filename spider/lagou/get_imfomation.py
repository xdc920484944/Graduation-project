from app.setting import MAX_PAGE
from app.spider.lagou.get_page import get_page
import time


def Get_imfomation(driver, job, city_code='', city=''):
    page = get_page(driver) if get_page(driver) < MAX_PAGE else MAX_PAGE
    if page > 1:
        page -= 1
    data = {}
    data[job] = []
    for p in range(page):
        lis = driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
        for l in lis:
            data[job].append(get_list(l, city))
        driver.find_element_by_xpath('//*[@id="order"]/li/div[4]/div[2]').click()
        time.sleep(1)
    return data


def get_list(l, city):
    l = l.text.split('\n')
    l[1] = l[1].replace('[', '').replace(']', '')  # [中关村] -> 中关村
    l[2] = deal_time(l[2])  # 时间处理
    l[3] = l[3].split(' ')[0]  # 5k-6k 经验不限 / 不限 -> 5k-6k
    result = [l[0], l[4], l[1], l[3], l[2], None, None, city]

    return result


# 时间处理
def deal_time(_time):
    base_time = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')
    day = 0
    list = [365, 30, 1]
    if '1天前发布' in _time:
        base_time[2] = int(base_time[2]) - 1
    elif '2天前发布' in _time:
        base_time[2] = int(base_time[2]) - 2
    elif '3天前发布' in _time:
        base_time[2] = int(base_time[2]) - 3
    elif '-' in _time:
        _time = _time.split('-')
        for i in range(len(_time)):
            _time[i] = int(_time[i])
            base_time[i] = int(base_time[i])
            day += (base_time[i] - _time[i]) * list[i]
        base_time[2] -= day
        if base_time[2] < 0:
            base_time[1] -= 1
            base_time[2] += 30
            if base_time[1] < 0:
                base_time[0] -= 1
                base_time[1] += 12
    base_time = str(base_time[0]) + '-' + str(base_time[1]) + '-' + str(base_time[2])

    return base_time


def creat_driver():
    chrome_options = Options()
    # 后面的两个是固定写法 必须这么写
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
