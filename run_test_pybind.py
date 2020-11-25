#!/usr/bin/env python3

import ctypes  
import ctypes.util  
import threading as T  
import time 
import numpy as np
import os
from timeit import timeit
import numba

@numba.jit(nopython=True, nogil=True)
def sum_range_numba(a: int):
    """Compute the sum of the numbers in the range [0, a)."""
    x = 0
    for i in range(a):
        # if i%3==0:
            x += i
    return x

# testname = ctypes.util.find_library('test')  
testlib = ctypes.cdll.LoadLibrary(os.getcwd()+"/libtest.so")  
#   
sum_range = testlib.sum_range
sum_range.argtypes = [ctypes.c_longlong]  
sum_range.restype = ctypes.c_longlong  

# import test_pybind
# add=test_pybind.add
# print()
# print("add(1,2) = {}".format(add(1,2)))
# sum_range=test_pybind.sum_range

high=100000000
high=1000000000
timeit_number=100

 
if __name__ == '__main__':  
    print() 
    print("sum_range({0}) = {1}".format(high, sum_range(high)))
    print() 
    print("timeit(sum_range({0})) = {1}".format(high, timeit(stmt='sum_range(high)', globals=globals(), number=timeit_number)))

    start_time = time.time()  
    for x in range(timeit_number):
        sum_range(high)  
        sum_range(high)  
    end_time = time.time()
    print() 
    print("Run time for {0} consecutive sequential double calls to the C library for sum_range in ms = {1:.4f}".format(timeit_number, 1000*(end_time - start_time)))  
    print()
    print("Run time (ms) taken for {0} consecutive sequential double calls to the C library for sum_range, as measured by timeit = {1}".format(timeit_number,1000*timeit(stmt="sum_range(high); sum_range(high)", globals=globals(), number=timeit_number)))
    print() 

    start_time = time.time()  
    for x in range(timeit_number):
        t1 = T.Thread(target=sum_range, args=(high,))  
        t2 = T.Thread(target=sum_range, args=(high,))  
        t1.start()  
        t2.start()  
        t1.join()  
        t2.join()  
    end_time = time.time()
    print("Run time for {0} consecutive parallel double calls to the C library for sum_range in ms: {1:.4f}".format(timeit_number, 1000*(end_time - start_time)))  
    print()
    print("Run time (ms) taken for {0} consecutive parallel double calls to the C library for sum_range, as measured by timeit = {1}".format(timeit_number,1000*timeit(stmt="t1 = T.Thread(target=sum_range, args=(high,));t2 = T.Thread(target=sum_range, args=(high,));t1.start();t2.start();t1.join();t2.join()", globals=globals(), number=timeit_number)))
    print() 

    # print("timeit('sum(range(iterations)') = {}".format(timeit('sum(range(iterations))', globals=globals())))
    # print() 
    # range_of_numbers=np.arange(high)
    # print("np.where(np.arange({0})%3==0,1,0).sum() = {1}".format(high, np.where(range_of_numbers%3==0,range_of_numbers,0).sum()))
    # print() 
    # print("timeit(np.where(np.arange({0})%3==0,range_of_numbers,0).sum()) = {1}".format(high, timeit('np.where(range_of_numbers%3==0,range_of_numbers,0).sum()', globals=globals(), number=timeit_number)))
    # print() 
    print("sum_range_numba({0}) = {1}".format(high, sum_range_numba(high)))
    print() 
    print("timeit(sum_range_numba({0})) = {1}".format(high, timeit('sum_range_numba(high)', globals=globals(), number=timeit_number)))
    print()
    start_time = time.time()  
    for x in range(timeit_number):
        t1 = T.Thread(target=sum_range_numba, args=(high,))  
        t2 = T.Thread(target=sum_range_numba, args=(high,))  
        t1.start()  
        t2.start()  
        t1.join()  
        t2.join()  
    end_time = time.time()
    print("Run time for {0} consecutive parallel double calls to the numba function for sum_range in ms: {1:.4f}".format(timeit_number, 1000*(end_time - start_time)))  
    print()
    print("Run time for {0} consecutive parallel double calls to the numba function for sum_range in ms, as measured by timeit = {1:.4f} ".format(timeit_number, timeit('t1 = T.Thread(target=sum_range_numba, args=(high,));t2 = T.Thread(target=sum_range_numba, args=(high,));t1.start();t2.start();t1.join();t2.join()', globals=globals(), number=timeit_number)))
    print()
