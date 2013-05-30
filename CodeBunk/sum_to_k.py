# Given a sorted integer array A of length N and an integer X,
# find if there exist 2 integers in A whose sum is equal to X. 
# Eg. A = [1,2,3,4,5], X=5, Ans = 1,4 or 2,3 (You need to print any one)

import random

def random_array(sz,low=10,high=100):
    return [random.randint(low,high) for i in xrange(sz)]

A = sorted(random_array(10))
X = random.randint(50,100)

def sum_k(lst,X):
    left,right = 0, len(lst) - 1
    while left < right:
        s = lst[left] + lst[right]
        if s == X:
            return (lst[left],lst[right])
        elif s > X:
            right -= 1
        else:
            left += 1
    return None
print A
print X
print sum_k(A,X)