from time import sleep, ctime
import multiprocessing

def super_player(file_,time):
    for i in range(2):
        print('Start playing:', file_,ctime())
        sleep(time)
lists={'愛情買賣.mp3':3,'阿凡達.mp4':5,'我和你.mp3':4}

threads=[]
files=range(len(lists))

#創建進程
for file_, time in lists.items():
    t=multiprocessing.Process(target=super_player, args=(file_, time))
    threads.append(t)

if __name__=='__main__':
    #啟動進程

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end',ctime())

#從執行結果並不能看出多進程multiprocessing與多線程threading之間的差異