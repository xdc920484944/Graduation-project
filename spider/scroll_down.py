#网页页面下拉
import time


def scroll_down(driver):
    for i in range(5):
        js = 'window.scrollTo(0,%s)' % (i * 4000)
        driver.execute_script(js)
        time.sleep(0.3)