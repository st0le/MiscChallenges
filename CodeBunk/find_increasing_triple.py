"""
Given an unsorted array if integers, find a triplet a,b,c where a<b<c and a appears before b which appears before c in the array.

For eg:
[1,3,6,-9, 2,0, 4]
Output = 1,3,6
"""

import random

def random_array(sz,low=10,high=100):
    return map(lambda _:random.randint(low,high), xrange(sz))

R = random_array(random.randint(5,20))


def find_increasing_triple(lst):
    
    sz = len(lst)
    if sz < 3: return None
    smaller_left = [-1] * sz
    greater_right = [-1] * sz
    min_index,max_index = 0,sz - 1
    # build smaller_left
    for i,v in enumerate(lst):
        if v <= lst[min_index]:
            min_index = i
        else:
            smaller_left[i] = min_index
            
    # build greater_right
    for i in xrange(sz - 1, - 1, -1):
        if lst[i] >= lst[max_index]:
            max_index = i
        else:
            greater_right[i] = max_index
    for i,(p,q) in enumerate(zip(smaller_left,greater_right)):
        if p >= 0 and q >=0:
          return lst[p],lst[i],lst[q]  
    return None

print R
print find_increasing_triple(R)