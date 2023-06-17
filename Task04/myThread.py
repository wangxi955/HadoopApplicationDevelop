# 使用threading模块创建线程
class myThread(threading.Thread):
    # 定义构造方法
    def __init__(self, threadID, name, counter, roomid, filename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.roomid = roomid
        self.filename = filename

    def run(self):
        bili(self.roomid, self.filename)
        print("开始线程：" + self.name)
        # 获取锁(实现线程同步)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()
        print("退出线程：" + self.name)

exitFlag = 0
# 为线程定义一个函数
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" %(threadName, time.ctime(time.time())))
        counter -= 1

if __name__ == "__main__":
    # 加锁防止多个进程保卫同一块数据
    threadLock = threading.Lock()
    thread1 = myThread(1, "Thread-1", 1, "3044248", "1.log")
    thread2 = myThread(2, "Thread-2", 2, "21669525", "2.log")
    thread3 = myThread(3, "Thread-3", 3, "5050", "3.log")
    thread4 = myThread(4, "Thread-4", 4, "545068", "4.log")
    thread5 = myThread(5, "Thread-5", 5, "7688602", "5.log")
    # 启动进程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    # 等待所有线程完成
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print("退出主线程")
