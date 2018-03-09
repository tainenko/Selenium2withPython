#定位一組元素
#Webdriver提供了8種定位一組元素的方法
#find_elements_by_id()
#find_elements_by_name()
#find_elements_by_tag_name()
#find_elements_by_link_text()
#find_elements_by_partial_link_text()
#find_elements_by_xpath()
#find_elements_by_css_selector()
#定位一組元素和定位單個元素的方法類似，唯一不同的地方是element後多加了一個s表示複數
from selenium import webdriver
import os, time

driver=webdriver.Firefox()
file_path='file://'+os.path.abspath('checkbox.html')
driver.get(file_path)

#選擇頁面上所有的tag name 為input的元素
inputs=driver.find_elements_by_tag_name('input')
#然後從中過濾出type為checkbox的元素，單擊勾選
for i in inputs:
    if i.get_attribute('type')=='checkbox':
        i.click()
        time.sleep(1)

driver.quit()