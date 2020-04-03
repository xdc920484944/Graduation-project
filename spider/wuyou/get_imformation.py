import time

import requests
import logging
from lxml import etree


def Get_imformation(url):
    '''
    无忧网详细信息爬取
    :param url:
    :return:获取招聘列表信息
    '''
    # logging.captureWarnings(True)
    res = requests.get(url, verify=False)
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.content)
    divs = html.xpath('//*[@id="resultList"]/div[@class="el"]')
    data = []
    for div in divs:
        occupation = div.xpath('./p/span/a')[0] \
            .text.replace(' ', '').replace('\n', '').replace('\r', '')
        company_name = div.xpath('./span[@class="t2"]/a')[0].text.replace(' ', '').replace('\n', '')
        address = div.xpath('./span[@class="t3"]')[0].text
        salary = div.xpath('./span[3]')[0].text
        release_time = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')[0]+'-' + \
                       div.xpath('./span[@class="t5"]')[0].text
        occupation_href = div.xpath('./p/span/a/@href')[0]
        company_href = div.xpath('./span[@class="t2"]/a/@href')[0]
        data.append([occupation, company_name, address, salary, release_time, occupation_href, company_href])

    return data


if __name__ == "__main__":
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,1.html"
    print(Get_imformation(url))