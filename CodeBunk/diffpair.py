"""
Give a sorted array of integers and an integer x, find if there are two elements whose difference is equal to x.

For eg:
A=[1, 3, 7, 19, 23] and x = 4
Output = True ((7,3) or (23,19))
"""
import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

arr = sorted(random_array(10,1,20))
K = random.randint(-20,20)

def diffpair(arr,K):
    i = j = 0
    while i < len(arr) and j < len(arr):
        if i != j and arr[i] == arr[j] + K:
            return arr[i],arr[j]
        if arr[i] < arr[j]+K:
            i += 1
        else:
            j += 1
    return None

#K = 0
print arr
print K
print diffpair(arr,K)

