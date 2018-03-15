import threading
from time import sleep, ctime
#創建線程類
#
class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self):
        self.func(*self.args)


def super_player(file_,time):
    for i in range(2):
        print('Start playing:',file_,ctime())
        sleep(time)
lists={'愛情買賣.mp3':3,'阿凡達.mp4':5,'我和你.mp3':4}

threads=[]
files=range(len(lists))

for file_,time in lists.items():
    t=threading.Thread(target=super_player,args=(file_,time))
    threads.append(t)

if __name__=='__main__':
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:',ctime())
