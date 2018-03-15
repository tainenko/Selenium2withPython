from time import sleep, ctime
#引進線程模塊
import threading

def music(func,loop):
    for i in range(loop):
        print('I was listening to ',func,ctime())
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print('I was at the ',func,ctime())
        sleep(5)

#創建線程t1，並添加到線程數組
threads=[]
tl=threading.Thread(target=music,args=('愛情買賣',2))
threads.append(tl)

#創建線程t2，並添加到線程數組
t2=threading.Thread(target=movie,args=('阿凡達',2))
threads.append(t2)

if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end:',ctime)