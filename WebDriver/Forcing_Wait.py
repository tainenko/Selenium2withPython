'''
利用pythom的time模塊裡的sleep()，讓腳本執行到某一位置時做固定時間的休眠
'''
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

sleep(2)
driver.find_element_by_id('kw').send_keys('webdriver')
driver.find_element_by_id('su').click()
sleep(3)

driver.quit()