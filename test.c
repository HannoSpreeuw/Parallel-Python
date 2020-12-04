// #include <stdio.h>
// 
#include <pybind11/pybind11.h>
namespace py = pybind11;

long long conditional_sum_range(long long to)
{
  long long i;
  long long s = 0LL;
 
  for (i = 0LL; i < to; i++)
    if (i % 3 == 0)
      s += i;

  return s;
}

int add(int i, int j) {
    return i + j;
}

long long sum_range(long long high)
{
  py::gil_scoped_release release;
  long long i;
  long long s = 0LL;
 
  for (i = 0LL; i < high; i++)
      s += (long long)i;

  return s;
}

// PYBIND11_MODULE(test_pybind, m) {
//     m.doc() = "pybind11 example plugin"; // optional module docstring
// 
//     m.def("sum_range", &test, "A function which adds up all numbers in a range which are a multiple of 3");
// }
// 
PYBIND11_MODULE(test_pybind, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("sum_range", &sum_range, "A function which adds upp numbers from 0 up to and including high-1");
}
