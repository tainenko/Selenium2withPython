import unittest

class Test(unittest.TestCase):

    def setUp(self):
        number=input("Enter a number:")
        self.number=int(number)

    #assertEqual(first,second,msg=None)
    #斷言first是否與second相等，如果不相等則測試失則，msg為可選參數，測試失敗時打印
    def test_case(self):
        self.assertEqual(self.number,10,msg='Your input is not 10!')

        def tearDown(self):
            pass

if __name__=='__main__':
    unittest.main()

'''
執行結果：
Enter a number:2
F
======================================================================
FAIL: test_case (__main__.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:/Github/selenium2withPython/Selenium2withPython/unittest/test_assert.py", line 10, in test_case
    self.assertEqual(self.number,10,msg='Your input is not 10!')
AssertionError: 2 != 10 : Your input is not 10!

----------------------------------------------------------------------
Ran 1 test in 2.448s

FAILED (failures=1)
'''