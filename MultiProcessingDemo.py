# -*- coding: utf-8 -*-

"""
多进程DEMO
"""
import time
import multiprocessing


def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.start()
    print("pid", p.pid)
    print("pname", p.name)
    print(("ps.isalive"), p.is_alive())
