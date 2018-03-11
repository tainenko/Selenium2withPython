'''
ScreenShoot
自動化測試是由程序去執行的，因此有時候打印的錯誤信息並不十分明確。如果在腳本執行出錯的時候能對當前窗口截圖保存，
那麼通過圖片就可以非常直觀地看出出錯的原因。Webdriver提供了截圖函數get_screenshot_as_file()來截取當前窗口。
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

#截取當前視窗畫面，並指定截圖的儲存路徑
driver.get_screenshot_as_file("D:\\baidu_img.png")

driver.quit()