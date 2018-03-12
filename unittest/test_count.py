from calculator import Count
#測試Count，兩個整數相加
class TestCount:
    def test_add(self):
        try:
            j=Count(2,3)
            add=j.add()
            #assert <test>, <message>  : test是狀態測試，而message是斷言失敗時所要呈現訊息。

            assert add==5,'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('Test pass!')

#執行測試類的測試方法
if __name__=='__main__':
    mytest=TestCount()
    mytest.test_add()

