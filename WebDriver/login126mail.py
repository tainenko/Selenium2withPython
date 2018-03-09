from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.126.com")
'''
2018/03/08
發現126mail已改成動態id，無法使用id定位
driver.find.element_by_id("idInput").clear()
driver.find.element_by_id("idInput").send_keys("username")
driver.find.element_by_id("pwdInput").clear()
driver.find.element_by_id("pwdInput").send_keys("password")
driver.find.element_by_id("loginBtn").click()
'''

'''
使用xpath定位也同樣失敗，查詢後發現其嵌套在表單frame/iframe中，
所以我們要先進入frame/iframe表單，然後再使用xpath定位
'''
#for Firefox
driver.switch_to.frame("x-URS-iframe")
#for Chrome
#driver.switch_to_frame(0)
time.sleep(5)
#定位到idInput，輸入帳號username
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input').send_keys('username')
#定位到passwardInput，輸入密碼passward
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').send_keys('passward')
#點擊登入按鈕
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a').click()
Thread.sleep(5000)
driver.quit()