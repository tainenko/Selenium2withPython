from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Baidu(unittest.TestCase):
    '''百度搜索測試'''
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url='http://www.baidu.com/'

    def test_baidu_search(self):
        '''搜索關鍵字:HTMLTestRunner'''
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys("HTMLTestRunner")
        driver.find_element_by_id('su').click()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    #按照一定格式獲取當前時間
    now=time.strftime('%Y-%m-%d %H_%M_%S')

    #定義報告儲存路徑
    filename='./'+now+'result.html'
    fp=open(filename,'wb')
    #定義測試報告
    runner=HTMLTestRunner(stream=fp,title='百度搜索測試報告',description='用例執行情況:')

    #運行測試用例
    runner.run(testunit)
    #關閉報告文件
    fp.close()