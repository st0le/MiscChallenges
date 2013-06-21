import sys

def is_jolly(line):
    lst = map(int,line.split())
    s = set(map(lambda i: abs(lst[i+1] - lst[i]), xrange(len(lst) - 1)))
    n = len(lst) - 1
    return ":)" if sum(s) == n * (n+1)/2 and len(s - set(xrange(n+1))) == 0 else ":("

print '\n'.join(map(is_jolly,sys.stdin.readlines()))