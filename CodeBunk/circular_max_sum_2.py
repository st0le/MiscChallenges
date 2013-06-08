import random

def random_array(sz,low=10,high = 100):
    return map(lambda _:random.randint(low,high),xrange(sz))

R = random_array(5,-10,10)
print "Actual Array :",R
print "Doubled Array : ",R+R

#extension of kadane's algorithm
def max_subarray_sum(lst):
    N = len(lst)
    mx = 0
    s = 0
    start,end = 0,0
    x,y = 0,0
    for i,v in enumerate(lst+lst): #cheating ;)
        if i - start >= N: #size of max array > size of array? cut off head and check if s is better?
            s -= lst[start]
            start = start + 1
            if mx < s : #because lst[start] can be negative at some point.
                mx = s
                x,y = start,end
        if s+v >= 0: # does new element make it negative?
            s = s + v
            end = i
        else:
            s = 0
            start = end = i + 1
        
        if mx < s : # sum better than previous best?
            mx = s
            x,y = start,end
    return mx,x % N,y % N
print max_subarray_sum(R)
    

#output is max_sum, start, end
# if end < start, it means list[end...] + lst[0..start]
    
