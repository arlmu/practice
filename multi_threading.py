#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, threading

#新线程执行的代码：
def loop():
    print('thread %s us running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('main %s thread is running...' % threading.current_thread().name)
#创建线程：
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
