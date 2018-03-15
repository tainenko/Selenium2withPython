from time import sleep , ctime
#創建了兩個任務:music, movie，並且通過sleep()來模擬任務的執行時間
def music():
    print('I was listening to music!',ctime())
    sleep(2)

def movie():
    print('Iwas at the movies!',ctime())
    sleep(5)


if __name__=='__main__':
    music()
    movie()
    print('all end:',ctime())
