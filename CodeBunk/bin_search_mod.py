"""
Given a sorted array, find if there is a number 'i' in the array such that A[i] = i.

For eg:
A=[-2, 0, 2, 4, 5]
Output = 2
"""
import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

def binary_search(A):
    lo = 0
    hi = len(A) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            hi = mid - 1
        else:
            lo = mid + 1
            
    return None

N = 15
R = sorted(set(random_array(N,0,N)))
#R = [-2, 0, 2, 4, 5]
print R
print "Valid Answers : ",filter(lambda i: i == R[i], xrange(len(R)))
print binary_search(R)
