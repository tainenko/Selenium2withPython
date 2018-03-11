'''
Javascript
webdriver提供了excute_script()方法來執行javascipt代碼，借助javascript可以控制瀏覽器的滾動條

調整滾動條位置的javascipt代碼如下：
window.scrollTo(左邊距,上邊距)
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#設置瀏覽器窗口大小
driver.set_window_size(600,600)

#搜索selenium
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

#通javascript設置瀏覽器窗口的滾動條位置
js='window.scrollTo(100,400);'
driver.execute_script(js)
sleep(3)

driver.quit()