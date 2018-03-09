#implicit Wait是通過一定的時長等待頁面上某元素加載完成。
#如果超出了設置的時長元素還沒有被加載，則拋出NoSuchElementException異常。
#implicit_wait()默認的等待時間為
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver=webdriver.Firefox()

#設置隱式等待為10秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
'''
執行結果:
Fri Mar  9 16:32:45 2018
Message: Unable to locate element: [id="kw22"]

Fri Mar  9 16:32:55 2018
當腳本執行到某個元素定位時，如果元素可定位，則繼續執行…，如果元素定位不到，則它將以輪詢的方式不斷地
判斷元素是否被定位到。假設在第6秒定位到了元素則繼續執行，若直到設置時長(10秒)都尚未定位到元素，則拋出
異常。

這此練習code當中，很明輸入框的定位id='kw22'有誤，通過print出來的兩個時間可以看出，執出對百輸入框的操作時，
超出了10秒的等待時間。
'''