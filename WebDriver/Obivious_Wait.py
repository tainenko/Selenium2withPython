#使用WebDriverWait顯式等待使Webdriver等待某個條件成立時繼續執行，否則在達到最大時長時拋棄超時界常(TimeoutException)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')

element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
element.send_keys('selenium')
driver.quit()