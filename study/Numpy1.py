import numpy as np
import time

# 使用for循环计算
a = np.random.rand(100000)
b = np.random.rand(100000)
c = 0
start = time.time()
for i in range(100000):
    c += a[i] * b[i]
end = time.time()
t = end - start
print("t=" + str(t))

# 使用numpy计算
start1 = time.time()
c1 = np.dot(a, b)
end1 = time.time()
t1 = end1 - start1
print("t1=" + str(t1))

print("t-t1=" + str(np.round(t / t1)))


def optimize(w, b):
    """

    :param w:
    :param b:
    :return:
    """

