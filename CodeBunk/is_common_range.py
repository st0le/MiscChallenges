"""

Given an unsorted array of +ve integers, find if the elements are consecutive.

For eg:
A=[12,15,11,13,14]
Output = True
A=[62, 60, 61, 61, 63]
Output = False (61 occurs twice)
"""

import random

lo = random.randint(-100,-100)
k  = random.randint(10,20)

arr = range(lo,lo+k)

random.shuffle(arr)

def is_complete_range2(arr):
    N = len(arr)
    mn = min(arr)
    for i in xrange(N):
        arr[i] -= mn
        if arr[i] >= N: return False
    return arr
    


def is_complete_range(arr):
    N = len(arr)
    mn = min(arr)
    for i in xrange(N):
        arr[i] -= mn
        if arr[i] >= N : return False
        
    for index in xrange(N):
        if arr[index] < N:
            node = arr[index]
            while node != index:
                if arr[node] >= N: return False
                arr[node] = arr[node] + N
                node = arr[node] % N
            arr[node] = arr[node] + N
    return True


print arr
print is_complete_range(arr)
print is_complete_range([12,15,11,13,14])
print is_complete_range([62, 60, 61, 61, 63])
print is_complete_range([6200, 60, 61, 61, 6300])
