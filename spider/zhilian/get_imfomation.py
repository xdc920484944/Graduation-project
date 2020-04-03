
from app.spider.fram import close_fram
import datetime
from app.spider.scroll_down import scroll_down
from app.spider.zhilian.get_page import get_page


def get_imfomation(driver, city, occupation):
    url = 'https://sou.zhaopin.com/?jl={}&sf=0&st=0&kw={}&kt=3'.format(city, occupation)
    print(url)
    driver.get(url)
    close_fram(driver, '/html/body/div[2]/div/div/button')    #关闭弹窗
    driver.get(url)
    page = get_page(driver)   #获取页数
    data = {}
    data[occupation] = []
    for p in range(page):
        url = 'https://sou.zhaopin.com/?p={}&jl={}&sf=0&st=0&kw={}&kt=3'.format(p+1, city, occupation)
        driver.get(url)
        scroll_down(driver)
        divs = driver.find_elements_by_xpath('//*[@id="listContent"]/div/div/a')
        release_time = datetime.datetime.now().strftime('%Y-%m-%d')
        for d in divs:
            occ_href = d.get_attribute('href')
            com_href = d.find_element_by_xpath('./div[1]/div[2]/a').get_attribute('href')
            d = d.text.split('\n')
            data[occupation].append([d[0], d[1], d[3], d[2], release_time, occ_href, com_href, city])
    return data