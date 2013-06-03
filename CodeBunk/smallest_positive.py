"""
Given an unsorted array of integers, find the smallest positive integer missing from the array.

For eg:
[2,5,3,8,-9, -1]
Output = 1
"""

import random

def random_array(sz,low=10,high=100):
    return [random.randint(low,high) for i in xrange(sz)]

A = random_array(10,-10,10)
#A = range(10)
#random.shuffle(A)

# modifies the original array.
def smallest_positive(A):

    # seperate negative and positive numbers 
    low,high = 0,len(A) - 1
    while low < high:
        while low < high and A[low] <= 0: low = low + 1
        while low < high and A[high] > 0: high = high - 1
        A[low],A[high] = A[high],A[low]
    #A[low..] contain all positive (excluding zero)
    #print A
    for i in xrange(1,len(A) - low + 1):
        x = abs(A[i+low-1])
        if x+low-1 < len(A) and A[x - 1 + low] > 0:
            A[x - 1 + low] *= -1
    # for each x in the positive end, mark A[x] as negative (we'll use this like a flag)
    for i in xrange(1,len(A) - low + 1):
        #the first positive number you encounter means, the index never occured in the postive end.
        if A[i - 1 + low] > 0:
            return i
    return len(A) - low + 1 #all were negative or marked off as negative? so the missing number is the max index of positive end
    
print A
print smallest_positive(A)