"""
Given an array of integers, find an index such that sum of elements before and after it is same. Print -1 if no such index exists.

For eg:
A=[-3, 2, 0, -1]
Output = 2 (A[0] + A[1] == A[3])
A=[-3, 2, 1, 4]
Output = 3 (A[0]+A[1]+A[2] == 0 (Sum of 0 elements))
"""

import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

def partition(arr):
    s = sum(arr)
    leftSum = 0
    for i,v in enumerate(arr):
        if leftSum == (s - v - leftSum): return i #s - v - leftSum is rightSum.
        leftSum += v
    return -1

arr = random_array(10,-10,10)

print partition([-3, 2, 0, -1])
print partition([-3, 2, 1, 4])
print arr
print partition(arr)