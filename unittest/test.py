from calculator import Count
#引入unittest模塊，創建TestCount類繼承unittest的TestCase類
#我們可以將TESTCase類看成是對特定類進行測試的集合。
import unittest
class TestCount(unittest.TestCase):
    
    #setUp()方法用於測試用例執行前的初始化工作。
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)


    #tearDown()方法與setUp()方法相呼應，用於測試用例執行之後的善後工作。
    def tearDown(self):
        print("test end")
if __name__=='__main__':
    unittest.main()