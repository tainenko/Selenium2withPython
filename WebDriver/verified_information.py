'''
在自動化測試執行完成之後，從頁面上獲取一些信息來証明測試結果是成功或失敗。
通常用得最多的幾種驗証信息分別是title、URL和text。
'''

from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('http://www.126.com')

print('Before login============')

#顯示當前頁面title
title=driver.title
print(title)

#顯示當前頁面url
now_url=driver.current_url
print(now_url)

#執行郵箱登錄
driver.switch_to.frame("x-URS-iframe")
#定位到idInput，輸入帳號username
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input').send_keys('username')
#定位到passwardInput，輸入密碼passward
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').send_keys('passward')
#點擊登入按鈕
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a').click()
time.sleep(5)

print('After login================')
#再次顯示當前頁面title
title=driver.title
print(title)

#再次顯示當前頁面url
now_url=driver.current_url
print(now_url)

#獲得登錄的用戶名
user=driver.find_element_by_id('spnUid').text
print(user)

driver.quit()

'''
執行結果：
Before login============
126网易免费邮--你的专业电子邮局
https://mail.126.com/
After login================
126网易免费邮--你的专业电子邮局
https://mail.126.com/

ps.帳號登入有驗証碼問題尚未克服
'''