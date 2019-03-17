# -*- coding: utf-8 -*-

"""
多进程DEMO
"""
import time
import multiprocessing
import os


def mult_file_reader(start_index, end_index, ):
    """
    多进程读取文件方法
    :param start_index: 开始读取标识
    :param end_index:  结束读取标识
    :return:
    """
    print("current pid:", os.getpid())
    print("start_index, end_index:", start_index, end_index)
    while start_index <= end_index:
        f = open("txt/" + str(start_index) + ".txt")
        line_list = f.readlines()
        for line in line_list:
            print(line)
        start_index += 1


def single_file_reader():
    """
    单线程读取文件
    :return:
    """
    for i in range(1, 4):
        f = open("txt/" + str(i) + ".txt")
        line_list = f.readlines()
        for line in line_list:
            print(line)


if __name__ == '__main__':
    # 测试多进程读取
    print("multi-processing start")
    m_start_time = time.process_time()
    pool = multiprocessing.Pool(processes=4)
    result = []
    work_range = int(4 / 2 - 1)
    print("work range:", work_range)
    start_index = 1
    i = 0
    while i < 2:
        pool.apply_async(mult_file_reader, (start_index, start_index + work_range,))
        i += 1
        start_index += (work_range + 1)

    pool.close()
    pool.join()
    m_end_time = time.process_time()
    m_time_cost = m_end_time - m_start_time
    print("all-process(es) done. cost:", round(m_time_cost, 4), "s")
    # 测试单线程读取
    print("single thread start")
    s_start_time = time.process_time()
    single_file_reader()
    s_end_time = time.process_time()
    s_time_cost = s_end_time - s_start_time
    print("single thread done. cost:", round(s_start_time, 4), "s")
    print("多进程/单线程 效率比为:", round(m_time_cost / s_time_cost, 2))
