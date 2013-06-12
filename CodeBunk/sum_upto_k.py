"""
For a +ve integer n, print all combinations of +ve integers which sum upto n.

For eg:
n=3
Output = ([1,2], [2,1], [1,1,1])
"""
import itertools

def sum_to_n(n,callback):
    def recurse(n,start,L):
        #print n,L
        if n == 0 and L:
            callback(L)
        else:
            for i in xrange(start,n+1):
                L.append(i)
                recurse(n - i,i, L )
                L.pop()
    recurse(n,1,[])

def all_combinations(n):
    res = []
    def add_permutations(L):
        l = res
        l.extend(sorted(set(itertools.permutations(L))))
    sum_to_n(n,add_permutations)    
    return res
    
for combo in all_combinations(5):
  print combo