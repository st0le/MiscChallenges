import itertools
for _ in xrange(input()):
    print max(len(list(b)) for a,b in itertools.groupby(raw_input().split(),key=len))
