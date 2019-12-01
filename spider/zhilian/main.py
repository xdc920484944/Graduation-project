from selenium import webdriver
from app.spider.zhilian.get_imfomation import get_imfomation
from selenium.webdriver.chrome.options import Options


# def creat_driver():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver


def get_data_zhilian(occupation, city, city_code=0):
    driver = webdriver.Chrome()
    data = get_imfomation(driver, city, occupation)
    return data

if __name__ == '__main__':
    city = '北京'
    occupation = '司机'
    data = get_data_zhilian(city=city, occupation=occupation)
    print(data)
