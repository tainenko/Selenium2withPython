#讀取user_info文件檔
user_file=open('user_info.txt','r')
lines=user_file.readlines()
user_file.close()

#逐行顯行文件檔裡頭的user & password資料
for line in lines:
    username=line.split(',')[0]
    password=line.split(',')[1]
    print(username,password)

'''
運行結果
zhangsan 123

lisi 456

wangwu 789
'''