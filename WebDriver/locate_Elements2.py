from selenium import webdriver
import os,time

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

#通過xpath定位type=checkbox的元素
#checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")

#通過css定位type=checkbox的元素
checkboxes=driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)
#顯示當前頁面上type為checkbox的個數
print(len(checkboxes))

#取消勾選頁面上最後一個checkbox
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
#pop() or pop(-1)默認選取一組元素裡的最後一個
#pop(0)                                                       第一個
#pop(1)                                                       第二個
#可以用pop(n)函數操作一組元素中任一個，只要知道欲操作的元素是第n個
driver.quit()
