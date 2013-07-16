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
print arr

def dp(arr):
    N = len(arr)
    X = [1] * N
    pi_x = [-1] * N
    Y = [1] * N
    pi_y = [-1] * N
    for i,v in enumerate(arr):
        for j in xrange(i):
            u = arr[j]
            if u < v and 1 + Y[j] > X[i]:
                X[i] = Y[j] + 1
                pi_x[i] = j
            if u > v and 1 + X[j] > Y[i]:
                Y[i] = X[j] + 1
                pi_y[i] = j
    mx_x = max(xrange(N),key=X.__getitem__)
    mx_y = max(xrange(N),key=Y.__getitem__)
    
    
    def backtrack(A,B,index):
        lst = []
        while index >= 0:
            lst.append(arr[index])
            index = A[index]
            A,B = B,A
        return lst
    
    if X[mx_x] < Y[mx_y]:
        return backtrack(pi_y,pi_x,mx_y)
    else:
        return backtrack(pi_x,pi_y,mx_x)
    
print dp(arr)
    
