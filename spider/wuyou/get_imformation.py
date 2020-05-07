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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.content)
    divs = html.xpath('//*[@id="resultList"]/div[@class="el"]')
    data = []
    for div in divs:
        occupation = div.xpath('./p/span/a')[0] \
            .text.replace(' ', '').replace('\n', '').replace('\r', '')  # 职位名
        company_name = div.xpath('./span[@class="t2"]/a')[0].text.replace(' ', '').replace('\n', '')  # 公司名
        address = div.xpath('./span[@class="t3"]')[0].text  # 工作地点
        salary = div.xpath('./span[3]')[0].text  # 薪资
        release_time = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')[0] + '-' + \
                       div.xpath('./span[@class="t5"]')[0].text  # 发布时间
        occupation_href = div.xpath('./p/span/a/@href')[0]  # 职位链接
        company_href = div.xpath('./span[@class="t2"]/a/@href')[0]  # 公式链接
        data.append([occupation, company_name, address, salary, release_time, occupation_href, company_href])

    return data


if __name__ == "__main__":
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,1.html"
    print(Get_imformation(url))
