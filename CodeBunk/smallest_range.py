"""
Given m sorted arrays, find a range which contains at least one number from each array and is smallest.

For eg:
a1=[1,2,4,8]
a2=[3,6,7,10]
a3=[4,9,10,13]
Output = (3,4)
"""

import random,pprint

def random_array(sz,low=10,high=100):
    return [random.randint(low,high) for i in xrange(sz)]


#M = [[1,2,4,8],[3,6,7,10],[4,9,10,13]]
M = map(sorted,[random_array(random.randint(5,10)) for i in xrange(random.randint(5,10))])
pprint.pprint(M)

#Complexity - O(m*n)
def common_range(lst):
    l = len(lst)
    inf = float('inf')
    indices = [0] * l
    start,end = -inf,inf
    while True:
        mn,mx = 0,0
        for i in xrange(l):
            if lst[mx][indices[mx]] < lst[i][indices[i]]:
                mx = i
            if lst[mn][indices[mn]] > lst[i][indices[i]]:
                mn = i
                
        if lst[mx][indices[mx]]-lst[mn][indices[mn]] < end-start:
            start,end = lst[mn][indices[mn]],lst[mx][indices[mx]]
        indices[mn] += 1
        if indices[mn] >= len(lst[mn]):
            break
    return (start,end)

print common_range(M)