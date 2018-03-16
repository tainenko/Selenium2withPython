import multiprocessing
import os, time

def inputQ(queue):
    info=str(os.getpid())+'(put):'+str(time.time())
    queue.put(info)

def outputQ(queue,lock):
    info=queue.get()
    lock.acquire()
    print(str(os.getpid())+'(get):'+info)
    lock.release()

if __name__=='__main__':
    record1=[]
    record2=[]
    #加鎖，為防止散亂的打印
    lock=multiprocessing.Lock()
    queue=multiprocessing.Queue(3)

    for i in range(10):
        process=multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)
    for i in range(10):
        process=multiprocessing.Process(target=outputQ,args=(queue,lock))
        record2.append(process)

    for p in record1:
        p.join()

    #沒有更多的對象進來，關閉queue
    queue.close()

    for p in record2:
        p.join()