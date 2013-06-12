"""
Given an array A of integers and a transformation defined as At[x] = A[x+1] - A[x].
Print the sum of the array transformed k times.
"""

import random

def random_array(sz,low=10,high=100):
    return map(lambda _:random.randint(low,high), xrange(sz))

R = random_array(10,1,9)
k = random.randint(3,6)

#R = [2,5,1,3,7,4]
#k = 3

def brute_force(A,k):
    for i in xrange(min(k,len(A))):
        A = map(lambda i:A[i+1] - A[i],xrange(len(A) - 1))
        print A
    return sum(A)

def not_so_smart_solution(A,k):
    
    binomial_row =[1]
    m = 1
    n = k + 1
    for j in xrange(1,n):
        m = m * (n - j) / j
        binomial_row.append(m * (-1 if j % 2 == 1 else 1))
    
    sm = 0
    for i in xrange(len(A)-len(binomial_row) + 1):
        s = sum(map(lambda (a,b):a*b,zip(binomial_row,A[i:])))
        #print s
        sm += s
    return sm * (-1 if k % 2 == 1 else 1)


print R,len(R)
print k
print brute_force(R,k)
print not_so_smart_solution(R,k)