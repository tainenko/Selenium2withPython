#下載文件
from selenium import webdriver
import os

#為了讓Firefox能實現下載文件，需要調整設定如下：
fp=webdriver.FirefoxProfile()
#browser.download.folderList，設置成0代表默認下載路徑，設置成2則可以保存到指定目錄
fp.set_preference("browser.download.folderList",2)
#是否顯示開始？ True為顯示，Flase為不顯示
fp.set_preference("browser.download.manager.showWhenStarting",False)
#用於指定下載文件的目錄，os.getcwd函數不需要傳遞參數，用於返回當前的目錄
fp.set_preference("browser.download.dir",os.getcwd())
#指定要下載頁面的Content_type值。
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")

driver=webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-3.10.0.tar.gz").click()