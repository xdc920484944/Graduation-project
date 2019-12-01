import re

from app.setting import MAX_PAGE
from app.spider.scroll_down import scroll_down


def get_page(driver):
    scroll_down(driver)
    driver.find_element_by_xpath('//*[@id="pagination_content"]/div/div/input').send_keys(99)
    driver.find_element_by_xpath('//*[@id="pagination_content"]/div/div/button').click()
    page = re.findall('p=([^&]*)', driver.current_url)
    page = int(page[0] if len(page) > 0 else 0)
    page = page if page <= MAX_PAGE else MAX_PAGE   #限制最大爬取页数
    return page