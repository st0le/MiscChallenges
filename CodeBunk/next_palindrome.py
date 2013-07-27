import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

#Time Complexity : O(log10(n))
def next_palindrome(n):
    if n < 9 : return n + 1 
    lst = map(int,str(n))
    N = len(lst)
    i = j = N/2
    if N % 2 == 0:
        i -= 1
    p,q = i,j
    while p >= 0 and lst[p] == lst[q]:
        p,q = p - 1, q + 1
    
    if p < 0 or lst[p] < lst[q]:
        while i >= 0:
            if lst[i] == 9:
                lst[i] = lst[j] = 0
            else:
                lst[i] = lst[j] = lst[i] + 1
                break
            i,j = i - 1, j + 1

    while p >= 0:
        lst[q] = lst[p]
        p,q = p - 1, q + 1

    def tonum(lst):
        np = 0
        for v in lst:
            np = np * 10 + v
        return np
    pal = tonum(lst)
    if pal == 0:
        lst[-1] = 1
        return tonum([1] + lst)
    else:
        return pal

def brute(n):
    
    def ispal(x):
        x = str(x)
        return x == x[::-1]
    n = n + 1
    while not ispal(n):
        n = n + 1
    return n

print next_palindrome(100) #tricky
print next_palindrome(99) #tricky
print next_palindrome(999)#tricky

for i in xrange(1500):
    p = next_palindrome(i)
    print i,p
    assert brute(i) == p

for v in random_array(10,10**9,10**10):
    p = next_palindrome(v)
    print v,p
    assert p == brute(v)
