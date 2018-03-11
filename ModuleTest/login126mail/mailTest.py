from selenium import webdriver
from public import Login

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.126.com")

#調用登錄模塊
Login().user_login(driver)

 #收信、寫信、刪除信件等操作
 #……

 #調用退出模塊
Login().user_logout(driver)