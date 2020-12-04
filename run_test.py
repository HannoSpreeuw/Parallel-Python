#!/usr/bin/env python3

import ctypes  
import ctypes.util  
import threading as T  
import time 
import numpy as np
import os
from timeit import timeit
import numba

@numba.jit
def sum_range_numba(a: int):
    """Compute the sum of the numbers in the range [0, a)."""
    x = 0
    for i in range(a):
        x += i
    return x

# testname = ctypes.util.find_library('test')  
testlib = ctypes.cdll.LoadLibrary(os.getcwd()+"/libtest.so")  
  
sum_range = testlib.sum_range  
sum_range.argtypes = [ctypes.c_long]  
sum_range.restype = ctypes.c_longlong  

iterations=100000

 
if __name__ == '__main__':  
    print() 
    print("sum_range(iterations) = {}".format(sum_range(iterations)))
    print() 
    print("timeit('sum_range(iterations)') = {}".format(timeit(stmt='sum_range(iterations)', globals=globals(), number=iterations)))
    start_time = time.time()  
    for x in range(iterations):
        sum_range(iterations)  
        sum_range(iterations)  
    end_time = time.time()
    print() 
    print("Sequential run time for {0} iterations of the C library for sum_range in ms = {1:.4f}".format(iterations, 1000*(end_time - start_time)))  
    print()
    print("Sequential run time (ms) taken for {0} iterations of the C library for sum_range, as measured by timeit = {1}".format(iterations,1000*timeit(stmt="sum_range(iterations); sum_range(iterations)", globals=globals(), number=iterations)))
    print() 

    start_time = time.time()  
    for x in range(iterations):
        t1 = T.Thread(target=sum_range, args=(iterations,))  
        t2 = T.Thread(target=sum_range, args=(iterations,))  
        t1.start()  
        t2.start()  
        t1.join()  
        t2.join()  
    end_time = time.time()
    print("Parallel run time for {0} iterations of the C library for sum_range in ms: {1:.4f}".format(iterations, 1000*(end_time - start_time)))  
    print()
    print("Parallel run time (ms) taken for {0} iterations of the C library for sum_range, as measured by timeit = {1}".format(iterations,1000*timeit(stmt="t1 = T.Thread(target=sum_range, args=(iterations,));t2 = T.Thread(target=sum_range, args=(iterations,));t1.start();t2.start();t1.join();t2.join()", globals=globals(), number=iterations)))
    print() 

    # print("timeit('sum(range(iterations)') = {}".format(timeit('sum(range(iterations))', globals=globals())))
    # print() 
    print("timeit('np.arange(iterations).sum()') = {}".format(timeit('np.arange(iterations).sum()', globals=globals(), number=iterations)))
    print() 
    print("timeit('sum_range_numba(iterations)') = {}".format(timeit('sum_range_numba(iterations)', globals=globals(), number=iterations)))
    print() 
    print("sum_range_numba(iterations) = {}".format(sum_range_numba(iterations)))
