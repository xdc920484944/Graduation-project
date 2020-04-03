import re
import requests
import logging
from lxml import etree

from app.setting import MAX_PAGE


def Get_page(url):
    '''
    页数爬取
    :param url:
    :return:
    '''
    try:
        logging.captureWarnings(True)
        res = requests.get(url, verify=False)
        res.encoding = res.apparent_encoding
        html = etree.HTML(res.content)
        html = html.xpath('//*[@id="resultList"]//span[@class="td"]')[0].text
        page = int(re.findall('(\d+)', html)[0])
        page = page if page < MAX_PAGE else MAX_PAGE
        return page
    except:
        print('页数获取失败:', url)

if __name__ == "__main__":
    url = "https://search.51job.com/list/050000,000000,0000,00,9,99,python,2,1.html?"
    page = Get_page(url)
    print(page)