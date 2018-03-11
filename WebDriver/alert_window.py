'''
警告框處理
首先通過switch_to_alert()方法定位到alert/confirm/prompt
然後使用以下方法進行操作
text                                返回alert/comfirm/prompt中的文字信息
accept()                          接受現有警告框
dismiss()                        解散現有警告框
send_keys(keysToSend)   發送文字內容"keysToSend"至警告框
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)

#鼠標懸停至“設置"
link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()

#打開搜索設置
driver.find_element_by_link_text("搜索设置").click()

#保存設置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)
#接受警告框
driver.switch_to.alert().accept()

driver.quit()
'''
Bug:無法定位到搜索設置。
'''