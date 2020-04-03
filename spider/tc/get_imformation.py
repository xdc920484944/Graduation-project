import re
import time


def change_date(date):
    or_date = time.strftime("%Y-%m-%d", time.localtime())
    s = or_date.split('-')
    y1 = int(s[0])
    m1 = int(s[1])
    d1 = int(s[2])
    if '今天' or '优选职位' in date:
        return or_date
    elif '天前' in date:
        d2 = int(date.replace('天前', ''))
        if d1 - d2 <= 0:
            m = m1 - 1
            d = d1 - d2 + 30
            if m == 2 and d > 29:
                d = 29
        else:
            m = m1
            d = d1 - d2
        if m <= 0:
            y = y1 - 1
            m += 12
        else:
            y = y1
            res = str(y) + '-' + str(m) + '-' + str(d)
    else:
        k = date.split('-')
        if len(k) == 2:
            res = str(y1) + '-' + date
        elif len(k) == 3:
            res = date
        else:
            print('日期转换错误:', date)
    return res


def Get_imformation(driver):
    '''
    获取职位列表数据
    :param url:
    :return: result:[[职位名,公司名,薪资,发布时间,职位链接,公司链接,福利,要求]，, []]
    '''

    job_imf = driver.find_elements_by_xpath('//li[@class="job_item clearfix"]/div[@class="item_con job_title"]')
    job_hrefs = driver.find_elements_by_xpath(
        '//li[@class="job_item clearfix"]/div[@class="item_con job_title"]/div/a')
    com_imf = driver.find_elements_by_xpath('//li[@class="job_item clearfix"]/div[@class="item_con job_comp"]')
    com_hrefs = driver.find_elements_by_xpath(
        '//li[@class="job_item clearfix"]/div[@class="item_con job_comp"]/div[@class="comp_name"]/a')
    date = driver.find_elements_by_xpath('//li[@class="job_item clearfix"]/*[@class="sign"]')
    data = []
    for n in range(len(job_imf)):
        try:
            job = job_imf[n].text.split('\n')
            com = com_imf[n].text.split('\n')
            job_name = job[0]  # 职位名
            salary = job[1]  # 薪资
            welfare = ''.join(j + '/' for j in job[2:])  # 福利
            com_name = re.findall('(.*) ', com[0])[0]  # 公司名
            require = com[1].replace(' ', '')  # 要求
            release_time = change_date(date[n].text)  # 发布时间
            job_href = job_hrefs[n].get_attribute('href')  # 职位链接
            com_href = com_hrefs[n].get_attribute('href')  # 公司链接
            data.append([job_name, com_name, salary, release_time, job_href, com_href, welfare, require])
        except Exception as e:
            print('数据爬取错误:', e)
            continue

    return data


if __name__ == "__main__":
    from app.spider.tc.main import creat_driver

    code = 'bj'
    page = 1
    key = '通信'
    # url = 'https://{}.58.com/job/pn{}/?key={}&classpolicy=job_A&final=1&jump=1'.format(code, page, key)
    url = 'https://bj.58.com/job/pn1/?key=java&classpolicy=job_A&final=1&jump=1'
    driver = creat_driver()
    driver.get(url=url)
    print(Get_imformation(driver))
    driver.close()
