"""
Given a finite stream of numbers, pick a number randomly. The probability of any number being chosen should be same.
"""
import random
N = 10
K = 4 #change it to 1 for solving the actual problem
arr = range(N)
random.shuffle(arr)

#http://en.wikipedia.org/wiki/Reservoir_sampling
def reservoir_sampling(stream,k): #sample k elements from stream
    sample = []
    stream_len = 0
    for v in stream:
        if len(sample) < k:
            sample.append(v)
        else:
            j = random.randint(0,stream_len)
            if j < k : sample[j] = v
        stream_len += 1
    return sample

def test():
    T = 100000
    freq = {}
    for v in arr: freq[v] = 0
    for i in xrange(T):
        sample = reservoir_sampling(arr,K)
        for v in sample: freq[v] += 1
    
    for v in freq:
        freq[v] /= float(K*T)
    print freq #should be close 1/N
    print "Ideal Probability : ", 1./N

test()            
print reservoir_sampling(arr,K)    
