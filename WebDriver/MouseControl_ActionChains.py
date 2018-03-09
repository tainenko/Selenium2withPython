'''
ActionChains:
perform():                  執行所有ActionChains中存儲的行為
context_click():           點擊右鍵
double_clilck():           雙擊左鍵
drag_and_drop():        拖動
move_to_element():    鼠標懸停
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http://yunpan.360.cn")
#點擊右鍵操作
#定位到要點擊右鍵的元素
right_click=driver.find_element_by_id("xx")
#對定位到的元素執行點擊右鍵的動作
ActionChains(driver).context_click(right_click).perform()

#懸停操作
#定位到要懸停的元素
above=driver.find_element_by_id("id")
#對定位到的元素執行懸停操作
ActionChains(driver).move_to_element(above).perform()

#雙擊操作
#定位到要雙擊的元素
double_click=driver.find_element_by_id("xx")
#對定位到的元素執行雙擊操作
ActionCHains(driver).double_click(double_click).perform()

#滑鼠拖放操作
#定位拖放起點的元素位置
element=driver.find_element_by_id("xx")
#定位元素要移動的目標位置
target=driver.find_element_by_id("yy")
#執行元素的拖放操作
ActionChains(driver).drag_and_drop(element,target).perform()

