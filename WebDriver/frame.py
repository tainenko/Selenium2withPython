'''
多表單切換：
webdriver只能在一個頁面上對元素識別與定位，遇到frmae/iframe表單嵌套頁面的應用時，
就需要通過switch_to.frame()方法將當前定位的主體切換為frame/iframe表單的內嵌頁面中。

'''
from selenium import webdriver
import os,time

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('frame.html')
driver.get(file_path)

#切換到iframe(id='f1')
driver.switch_to.frame("f1")
#再切換到iframe(id='f2')
driver.switch_to.frame("f2")
'''
也可以用xpath先定位到iframe，再將定位對象傳給waitch_to.frome()，具體作法如下
xf1=driver.find_element_by_xpath('//*[@class="f1"]')
driver.switch_to.frame(xf1)

xf2=driver.find_element_by_xpath('//*[@class="f2"]')
driver.switch_to.frame(xf2)
'''
#切換至frame id=f2後就可以正確的定位到元素了
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)

#完成了在當前表單上的操作後，可以通過switch_to.parene_frame()跳回前一級的表單
driver.switch_to.parent_frame()
time.sleep(3)

#除此之外，在進入到多級表單的情況下，可以通過switch_to.default_contant()跳回最外層的頁面
driver.switch_to.default_content()
time.sleep(3)

driver.quit()