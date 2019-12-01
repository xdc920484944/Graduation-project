def get_page(driver):
    page = int(driver.find_element_by_xpath('//*[@id="order"]/li/div[4]/div[3]/span[2]').text)
    return page