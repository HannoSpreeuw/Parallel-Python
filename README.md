# Parallel-Python
Code and scripts exploring performance of parallel python, ctypes, pybind11, Numba, numpy and pure Python all in one go

Compile and link for ctypes using
```
gcc -O3 -g -fPIC -c -o test.o test.c
ld -shared -o libtest.so test.o
```
Compile and link for pybind11 using
```
c++ -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` test.c -o test_pybind`python3-config --extension-suffix`
```
or add a `-O3` there.
Renaming seems necessary or the library will not be imported:
```
mv test_pybind.cpython-37m-x86_64-linux-gnu.so test_pybind.so
```
