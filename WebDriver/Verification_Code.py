'''
webdriver並沒有提供相應的方法來處理驗証碼。
1.去掉驗証碼：
2.設置萬能驗証碼：
3.驗証碼識別技術：
通過python-tesseract來識別圖片驗証碼。
4.記錄cookies：
詳細操作記錄於Verification_Cookies.py
'''

from random import randint

verify=randint(1000,9999)
print("生成的隨機數",verify)

number=input("請輸入隨機數:")
print(number)
number=int(number)

if number==verify:
    print("登錄成功!!")
elif number==132741:
    print("登錄成功!!")
else:
    print("驗証碼輸入有誤!")
'''
執行結果
========================
生成的隨機數 7274
請輸入隨機數:132741
132741
登錄成功!!
========================
生成的隨機數 1198
請輸入隨機數:1198
1198
登錄成功!!
========================
生成的隨機數 2856
請輸入隨機數:1198
1198
驗証碼輸入有誤!
'''