from selenium import webdriver
from app.spider.zhilian.get_imfomation import Get_imformation
from selenium.webdriver.chrome.options import Options


def get_data_zhilian(key):
    '''
    :param key: 搜索的职业
    :return:
    '''
    return Get_imformation(key)


if __name__ == '__main__':
    # https://sou.zhaopin.com/?jl=530&kw=Python&kt=3
    city = '北京'
    occupation = '司机'
    data = get_data_zhilian(city=city, occupation=occupation)
    print(data)
