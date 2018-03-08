'''
Practice of the webdriver function as below:
size:                             gett the size of element
text:                             get the text of element
get_attribute(name):       get the attribute value of name
is_displayed():               check the visible of element, if yes return True.
'''
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#獲得輸入框的尺吋
size=driver.find_element_by_id("kw").size
print(size)

#返回百度頁面底部備案信息
text=driver.find_element_by_id('cp').text
print(text)

#返回元素的屬性值，可以是id name type或其他任意屬性
attribute=driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

#確認元素是否可見，使用者可見返回True，不可見返回False
visible=driver.find_element_by_id('kw').is_displayed()
print(visible)

driver.quit()

'''
執行結果：
{'height': 22.0, 'width': 500.0}
©2018 Baidu 使用百度前必读 意见反馈 京ICP证030173号  京公网安备11000002000001号 
text
True
'''