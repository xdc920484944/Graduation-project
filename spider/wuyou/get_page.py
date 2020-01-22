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
        page = int(int(re.findall('(\d+)', html)[0]) / 50) + 1
        page = page if page < MAX_PAGE else MAX_PAGE
        return page
    except:
        print('页数获取失败:', url)
