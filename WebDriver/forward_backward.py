from selenium import webdriver
driver=webdriver.Firefox()

#Visit www.baidu.com
first_url='http://www.baidu.com'
driver.get(first_url)
print("now access",first_url)

#Visit news.baidu.com
second_url='http://news.baidu.com'
driver.get(second_url)
print("now access",second_url)

#back to www.baidu.com
driver.back()
print("back to ",first_url)

#forward to new.baidu.com
driver.forward()
print("forward to",second_url)

driver.refresh()
driver.quit()