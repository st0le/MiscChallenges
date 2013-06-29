'''
1. Set a = Arr[0]
2. Till b is not found, any number < a should be made 'a'.
3. Once 'b' is found, any number < b and > a becomes the new 'b'. Number < a stored in a different var 
called minval. If a number >b is encountered, problem solved.
4. If you have a != minval then this means you can discard the old pair of a,b with minval and new number if you find a number < b.
'''

import random

def random_array(sz,low=10,high=100):
    return map(lambda _:random.randint(low,high), xrange(sz))

R = random_array(random.randint(5,10))

def find_triple(A):
    if len(A) <= 2:
        return None
    min_val = a = A[0]
    b = None
    
    for v in A[1:]:
      if min_val>v:
        min_val = v
      elif b==None or b > v :
        a,b = min_val,v
      else:
        return a,b,v
        
        
    return None
print R
print find_triple(R)