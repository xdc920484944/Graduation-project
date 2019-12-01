from selenium import webdriver
from app.spider.lagou.get_imfomation import Get_imfomation


def get_data_lagou(occupation, city, city_code=''):
    url = 'https://www.lagou.com/jobs/list_{}?&px=default&city={}'.format(occupation, city)
    driver = webdriver.Chrome()
    driver.get(url)
    data = Get_imfomation(driver, occupation, city=city)
    return data


if __name__ == '__main__':
    job = 'python'
    city = '福州'
    data = get_data_lagou(job, city)
    print(data)
