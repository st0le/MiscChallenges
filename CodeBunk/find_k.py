"""
Consider an array of integers with a property that consecutive elements differ by at most 1. Given a number k, find if it exists in this array.

For eg:
[2,2,1,2,3,4,3] and k=1
Output = True
"""
import random

def new_array(sz):
  R = [random.randint(10,20)]
  for i in xrange(sz-1):
    R.append(random.randint(-1,1) + R[-1])
  return R
R = new_array(10)
print R


# if s = abs(R[i] - k) is not zero,then clearly we will not find k for the next s-1 elements. 
def find_k(lst,K):
  i,sz = 0,len(lst)
  while i < sz:
    print lst[i:] #debug, to show the unsearched part of the array
    s = abs(K-lst[i]) 
    if s == 0: return i #found K, yay!
    else: i += s #we can skip the next s - 1 elements, it's guaranteed not to contain K
  return -1 #not found. :(



K = R[-1] #random.randint(10,20)
print "K = ", K
print find_k(R,K)
