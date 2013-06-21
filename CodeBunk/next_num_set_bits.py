"""
Given a +ve integer n, sort numbers from 1 to n with increasing number of bits set. If two numbers have same number of bits set, the lower number will come first.

For eg:
n=4
Output = 1,2,4,3
(1=0001, 2=0010,4=0100 i.e. 1 bit set. 3 = 0011 i.e. 2 bits set)
"""

#from hackers delight. I'm not that smart. ;)
def next_num(n):
    if n == 0: return 0
    lowbit = n & -n
    ripple = n + lowbit
    ones = n ^ ripple
    ones = (ones >> 2)/lowbit
    return ripple|ones

def foo_generator(n):
    bits_set = 1
    while True:
        x = (1<<bits_set) - 1
        if x > n: break
        while x < n:
            yield x
            x = next_num(x)
        bits_set += 1


for i in foo_generator(100):
    print i,bin(i)[2:]
