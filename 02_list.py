# coding:utf-8

import timeit
from timeit import Timer
li1 = [1,2]
li2 = [3,4]


def test1():
    li = [i for i in range(10000)]


time1 = Timer('test1','from __main__ import test1')
print(time1.timeit(1000))