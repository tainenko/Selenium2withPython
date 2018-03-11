import csv
#讀取csv檔案
data=csv.reader(open('info.csv','r'))

#print資料中的mail欄位
for user in data:
    print(user[1])

'''
執行結果
123456@126.com
123456@qq.com
123456@128.com
 '''
