'''
Uploadfile
對於通input標簽實現的上傳功能，可以將其看作是一個輸入框，即通過send_keys()
指定本地文件路徑的方式實現文件上傳
'''
from selenium import webdriver
import os
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('upfile.html')
driver.get(file_path)

#定位上傳按鈕，添加上傳文件路徑
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')

driver.quit()