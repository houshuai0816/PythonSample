import threading
import time
import _thread
import _threading_local


class myThread(threading.Thread):
    def __int__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("Starting"+self.name)
        #获取锁，成功获的锁后返回True
        #可选的timeout参数不填时将一直阻塞知道获取锁定
        #否则超时后但会False
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        # 释放锁
        threadLock.release()


def print_time(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName,time.ctime(time.time())))
            counter-=1

threadLock=threading.Lock
threads=[]
# 开启新线程
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)
# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("Exiting Main Thread")





