from selenium import webdriver
#practice of submit() function
driver=webdriver.Firefox()
driver.get("http://www.youdao.com")
#在輸入框鍵入 hello
driver.find_element_by_id('translateContent').send_keys('hello')
#提交輸入框的內容
driver.find_element_by_id("translateContent").submit()
driver.quit()