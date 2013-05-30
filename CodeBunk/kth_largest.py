"""
Bunk has a problem:

Given two sorted arrays, A & B, find the kth largest element in the combined array i.e sort(uniq(A+B)).

For eg:
A=[1,3,4]
B=[2,4,6,8]
K=3
Output = 4
"""

import random
N = 5
def random_array(sz,low=10,high=100):
    return [random.randint(low,high) for i in xrange(sz)]
A,B = random_array(N+random.randint(0,N)),random_array(N+random.randint(0,N))
A.sort()
B.sort()

# linear algorithm ~ O(k)
def find_kth_largest(A,B,k):
    if k <= 0 or k > len(A) + len(B):
        raise Exception("invalid value of k")
    i,j = len(A) - 1,len(B) - 1
    kth_elem = None
    while i >= 0 and j >= 0 and k > 0:
        kth_elem = max(A[i],B[j])
        while i >= 0 and A[i] == kth_elem: i -= 1
        while j >= 0 and B[j] == kth_elem: j -= 1
        k -= 1
    while i >= 0 and k > 0:
        kth_elem = A[i]
        while i >= 0 and A[i] == kth_elem: i -= 1
        k -= 1
    while j >= 0 and k > 0:
        kth_elem = B[j]
        while j >= 0 and B[j] == kth_elem: j -= 1
        k -= 1
    return kth_elem

K = random.randint(1,2*N)
print A
print B
print "K = ",K
print find_kth_largest(A,B,K)