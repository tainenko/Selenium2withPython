from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

search_windows=driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

all_handles=driver.window_handles

#進入注冊視窗
for handle in all_handles:
    if handle !=search_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('username')
        driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys('password')
        time.sleep(2)

#進入搜索視窗
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window!')
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)

driver.quit()

'''
執行結果：
It works on Chorme, but Firefox fail to excute.

Firefox would be failed  to locate the link_text('登录')
the bug need to be fixed 
'''