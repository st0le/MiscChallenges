from itertools import groupby
import sys

def encode(input_string):
    return ''.join(["%d%s"%(len(list(g)), k) for k,g in groupby(input_string.strip())])


print '\n'.join(map(encode,sys.stdin.readlines()))