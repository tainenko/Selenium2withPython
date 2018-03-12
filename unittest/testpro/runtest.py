'''
對範例的test.py文件的測試用例進行拆分，拆分後的目錄結構如下：
testpro/
|---calculator.py
|---testadd.py
|---testsub.py
|---runtest.py
拆分後的好處是可以依照所測試的功能進行分類，當單元測試用例變龐大時，後期維護時比較方便

'''

import unittest

import testadd
import testsub

suite=unittest.TestSuite()

suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testsub.TestSub("test_sub"))
suite.addTest(testsub.TestSub("test_sub2"))

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)
