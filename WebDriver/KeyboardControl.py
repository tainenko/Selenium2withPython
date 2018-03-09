'''
模擬鍵盤按盤與組合鍵的各種用法

使用鍵盤按鍵方法前需要先導入keys類
from selenium.webdriver.common.keys import Keys

以下為常用的鍵盤操作：
send_keys(Keys.BACK_SPACE)              刪除鍵
send_keys(Keys.SPACE)                         空格鍵
send_keys(Keys.TAB)                             制表鍵
send_keys(Keys.ESCAPE)                       回退鍵
send_keys(Keys.ENTER)                         回車鍵
send_keys(Keys.CONTROL,'a')                全選ctrl+a
send_keys(Keys.CONTROL,'c')                複製ctrl+c
send_keys(Keys.CONTROL,'x')                剪下ctrl+x
send_keys(Keys.CONTROL,'v')                貼上ctrl+v
send_keys(Keys.F1)                                 鍵盤F1
......                                                        .....
send_keys(Keys.F12)                               鍵盤F12

'''
from selenium import webdriver
#import Keys模塊
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#輸入框輸入內容
driver.find_element_by_id("kw").send_keys("seleniumm")

#刪除多輸入的一個m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#輸入空格鍵+"教程"
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

#ctrl+a 全選輸入框內容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

#ctrl+x 剪下輸入框內容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

#ctrl+v 貼上內容到輸入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#輸入Enter鍵送出
driver.find_element_by_id('kw').send_keys(Keys.ENTER)

driver.quit()