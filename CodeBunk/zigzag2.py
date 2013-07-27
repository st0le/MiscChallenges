"""
Given an array of integers, print the length of longest subsequence with the following property.
X[0]>X[1]<X[2]>X[3]<...<X[i]>X[i+1]<X[i+2]...
Eg:
A = [1,5,3,2,4]
Output = 3 ([5,3,4] or [5,2,4])
"""
import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))


arr = list(set(random_array(10)))


def zigzag(arr):
    res = []
    N = len(arr)
    inc = False
    last = 0
    for i in xrange(N-1):
        if (inc and arr[i] < arr[i+1]) or (not inc and arr[i] > arr[i+1]):
            res.append(arr[i])
            inc = not inc
            last = arr[i+1]
    res.append(last)
    return res
    

print arr
print zigzag(arr)