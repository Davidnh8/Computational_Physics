import numpy as np
import matplotlib.pyplot as plt
import random
import time


cdef int i
cdef int N
cpdef cython1():
    for i in range(50000000):
        N=i