import numpy as np
from numba import jit
import time

size = 1000
x = np.random.rand(size, size)
iterations = 1000


@jit(nopython=True)
def numba(a):
    c = np.zeros((size, size))
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i, j] = a[i, j] + 1
    return c


def lambda_run(a):
    return a.apply(lambda x: x + 1)

def vectorized(a):
    return np.where(a < 0.5, 1, 0)

# Call the numba function to precompile it before time measurement
z = numba(x)
start = time.time()
for _ in range(iterations):
    z = numba(x)
end = time.time()
print("Elapsed (numba, precompiled) = %s" % (end - start))

start = time.time()
for _ in range(iterations):
    z = vectorized(x)
end = time.time()
print("Elapsed (vectorized) = %s" % (end - start))
