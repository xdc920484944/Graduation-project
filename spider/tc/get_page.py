from app.setting import MAX_PAGE


def Get_page(driver):
    page = int(driver.find_element_by_xpath('/html/body//div[@class="pages clearfix"]//span[@class="total_page"]').text)
    return page if page < MAX_PAGE else MAX_PAGE