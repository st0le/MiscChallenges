# Reference : http://algnotes.wordpress.com/2012/09/23/maximum-circular-subarray/
import random

def random_array(sz,low=10,high = 100):
    return map(lambda i:random.randint(low,high),xrange(sz))

R = random_array(5,-10,10)

print R


def max_subarray_sum(lst):
    def kadane(L,mul=1):
        s = mx = 0
        for v in L:
            s = max(s+v*mul,0)
            mx = max(mx,s)
        return mx
    return max(kadane(lst),sum(lst)+kadane(lst,-1))
print max_subarray_sum(R)
