from selenium import webdriver
from public import Login

class LoginTest():
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.126.com")

    #admin用戶登錄
    def test_admin_login(self):
        username='admin'
        password='123'
        Login().user_login(self.driver,username,password)
        self.driver.quit()
    #guest用戶登錄
    def test_guest_login(self):
        username='guest'
        password='321'
        Login().user_login(self.driver,username,password)
        self.driver.quit()

if __name__=='__main__':
    LoginTest().test_admin_login()
    LoginTest().test_guest_login()