"""
For a +ve integer n, print numbers from 0 to 2^n-1 such that numbers next to each other differ in exactly 1 bit.
"""
n = 3
gray  = lambda x : (x >> 1) ^ x
pad_right = lambda s,l: ''.join(['0']*(l-len(s))) + s
for i in xrange(1 << n):
    print i,pad_right(bin(gray(i))[2:],n)
