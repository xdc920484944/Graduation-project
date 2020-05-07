import random
import requests
from lxml import etree
from app.setting import MAX_LINE
from app.spider.tc.main import creat_driver


# tc数据格式：{搜索关键字:[[职位名(0),公司名(1),薪资(2),发布时间(3),职位链接(4),公司链接(5),福利(6),要求(7),城市(8)], [],...]}

def Get_content(data):
    '''
    :param data:源数据
    :return: {url1:[职位名(0),公司名(1),薪资(2),发布时间(3),福利(4),学历要求(5),工作经验(6),详情(7)], url2:[]}
    '''
    def get_urls():
        '''
        获取所有职位信息的url
        :param data: {搜索关键字:[[职位名(0),公司名(1),薪资(2),发布时间(3),职位链接(4),公司链接(5),福利(6),要求(7),城市(8)], [],...]}
        :return: [job_url1,job_url2,...], [com_url1,com_url2,...]
        '''
        w_f_value = list(data.values())[0]
        num = MAX_LINE if len(w_f_value) > MAX_LINE else len(w_f_value)
        job_url_list = []
        com_url_list = []
        for values in random.sample(w_f_value, num):
            job_url = values[4]
            com_url = values[5]
            job_url_list.append(job_url)
            com_url_list.append(com_url)
        return job_url_list, com_url_list

    def get_content(url):
        '''
        :param url:
        :return:[职位名,公司名,薪资,发布时间,福利,学历要求,工作经验,详情]
        '''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding
        html = etree.HTML(res.content)
        salary = html.xpath('/html/body//span[@class="pos_salary"]')[0].text
        com_name = html.xpath('/html/body//div[@class="baseInfo_link"]')[0].text
        release_time = html.xpath('/html/body//span[@class="pos_base_num pos_base_update"]/span')[0].text
        job_name = html.xpath('/html/body//span[@class="pos_title"]')[0].text
        welfare = '/'.join(s.text for s in html.xpath('/html/body//span[@class="pos_welfare_item"]'))
        jobdegree = html.xpath('/html/body//span[@class="item_condition"]')[0].text
        exp = html.xpath('/html/body//span[@class="item_condition border_right_None"]')[0].text
        content = ''.join(c for c in html.xpath('/html/body//div[@class="des"]/text()')[0:-4])
        result = [job_name, com_name, salary, release_time, welfare, jobdegree, exp, content]
        return result

    job_urls, com_urls = get_urls()
    job_imf = {}
    com_imf = {}
    for url in job_urls:
        try:
            job_imf[url] = get_content(url)
        except Exception as e:
            print(e, url)
            continue
    return job_imf, com_imf


if __name__ == '__main__':
    Get_content()
