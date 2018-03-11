'''
通過向瀏覽器中添加cookie可以繞過登錄的驗証碼。
例如我們在第一次登錄某網站時勾選“記住密碼“的選項，當下次再訪問該網站時自動就處於登錄狀態了。
'''
from selenium import webdriver

driver=webdriver.Firefox()
#訪問xx網站
driver.get('http://www.xx.cn')

#將用戶名稱及密碼寫入瀏覽器cookie
driver.add_cookie({'name':'Login_UserNumber','value':'username'})
driver.add_cookie({'name':'Login_Passwd','value':'password'})
#再次訪問xx網站，將會自動登錄
driver.get('http://www.xx.cn')

driver.quit()