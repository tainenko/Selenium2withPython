from calculator import Count
import unittest

#當setUp()和tearDown()所做的事情是每個用例都需要的時候，可以自行獨立成一個類
#如此一來注意力便可專注在具體用例的編寫上。
class MyTest(unittest.TestCase):

    def setUp(self):
        print('test case start')

    def tearDown(self):
        print("test case end")


class TestAdd(MyTest):
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


class TestSub(MyTest):
    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)

if __name__=='__main__':
    unittest.main()