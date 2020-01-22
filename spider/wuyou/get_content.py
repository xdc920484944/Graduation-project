import requests
from lxml import etree


def Get_Job_Information(urls):
    '''
    获取职位信息
    :param urls: 职位信息url
    :return:[]
    '''
    try:
        for url in urls:
            res = requests.get(url)
            res.encoding = res.apparent_encoding
            html = etree.HTML(res.content)
            html = html.xpath('/html/body//div[@class="bmsg job_msg inbox"]//p//text()')
            text = ''
            result = []
            for t in html:
                text += t
            result.append(text)
        # print(result)
        return result
    except:
        print('获取招聘详细信息失败:', url)


if __name__ == '__main__':
    url = ['https://jobs.51job.com/xiamen/119802274.html?s=01&t=0']
    Get_Job_Information(url)
