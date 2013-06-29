"""
Given an array of length N and two integers 0<=i,j<N, find the position of min(A[i to j]).

For eg:
A=[2,4,7,1,5,9,3,5,7,4], i=2, j=7
=>A[i to j] = [7,1,5,9,3,5]
Output = 3 (Index of 1 in A)
"""
import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

# Time Complexity : Query O(n)
# Space Complexity : O(1)
def min_array_1(arr):
    return lambda i,j : min(xrange(i,j+1),key = arr.__getitem__)

# Time Complexity : O(n^2), Query O(1)
# Space Complexity : O(n^2)
def min_array_2(arr):
    min_ds = []
    N = len(arr)
    for i in xrange(N):
        row = []
        mn = i
        for j in xrange(i,N):
            if arr[mn] > arr[j]: mn = j
            row.append(mn)
        min_ds.append(row)
    min_func = lambda i,j : min_ds[i][j-i]
    return min_func
    

# Time Complexity : O(n), Query O(sqrt(n))
# Space Complexity : O(sqrt(n))
def min_array_3(arr):
    N = len(arr)
    sqrt = int(N**.5)
    min_ds = []
    for i in xrange(0,N,sqrt):
        mn = i
        for k in xrange(i,min(i+sqrt,N)):
            if arr[k] < arr[mn] : mn = k
        min_ds.append(mn)
    
    def min_func(i,j):
        k = i
        mn = i
        while k <= j and k % sqrt > 0:
            if arr[k] < arr[mn]: mn = k
            k += 1
        while k + sqrt <= j:
            if arr[min_ds[k/sqrt]] < arr[mn]  : mn = min_ds[k/sqrt]
            k += sqrt
        while k <= j:
            if arr[k] < arr[mn]: mn = k
            k += 1
        return mn
    
    return min_func

# Time Complexity : O(nlogn), Query O(1)
# Space Complexity : O(nlogn)
def min_array_4(arr):
    N = len(arr)
    logN = 0
    while 1 << logN  < N: logN += 1
    M = [[i] for i in xrange(N)]
    
    for j in xrange(1,logN + 1):
        step = 1 << j
        for i in xrange(N - step + 1):
            if arr[M[i][j-1]] < arr[M[i + step/2][j-1]]:
                M[i].append(M[i][j-1])
            else:
                M[i].append(M[i + step/2][j-1])
    
    def min_func(i,j):
        gap = j - i + 1
        k = 0
        while (1<< (k+1)) <= gap: k += 1 #note k = log(j-i+1)
        return M[i][k] if arr[M[i][k]] < arr[M[j - (1<<k) + 1][k]] else  M[j - (1<<k) + 1][k]
    
    return min_func

# Time Complexity : O(n), Query O(logn)
# Space Complexity : O(2 * 2^(logN+1))
def min_array_5(arr):
    N = len(arr)
    segment_tree = {}
    
    def build_tree(st,node,start,end):
        if start == end:
            st[node] = start
        else:
            mid = (start+end)/2
            left,right = build_tree(st,2*node + 1, start, mid),build_tree(st,2*node + 2, mid + 1,end)
            st[node] = left if arr[left] < arr[right] else right
        return st[node]
    
    build_tree(segment_tree,0,0,N - 1)
    
    def min_func(i,j,node = 0, begin = 0, end = N - 1):
        if i > end or j < begin:
            return None
        if begin >= i and end <= j:
            return segment_tree[node]
        mid = (begin + end) / 2
        left,right = min_func(i,j,2*node+1,begin,mid),min_func(i,j,2*node+2,mid+1,end)
        if left is not None and right is not None:
            return left if arr[left] < arr[right] else right
        else:
            return left if left is not None else right
    return min_func



def test(min_algo,testcases=5,N=10):
    R = random_array(N)
    min_func = min_algo(R)
    print R
    for i in xrange(testcases):
        i,j = random.randint(0,N - 1),random.randint(0,N - 1)
        if i > j : i,j = j,i
        k = min_func(i,j)
        verify = min(xrange(i,j+1),key=R.__getitem__) #same as algo 1
        assert R[verify] == R[k], "A[%d..%d] -> %d != %d" % (i,j,k,verify)
        print "Minimum element between A[%d..%d] is A[%d] = %d"% (i,j,k,R[k])

if __name__ == '__main__':
    
    test(min_array_1) # Linear Scan - Time/Query : O(n)
    test(min_array_2) # Brute Force DP - Time : O(n^2) / Query : O(1) / Space : O(n^2)
    test(min_array_3) # RMQ-Blocks - Time : O(n) / Query : O(sqrt(n)) / Space : O(n)
    test(min_array_4) # DP-2^k Intervals - Time : O(nlogn) / Query : O(1) / Space : O(nlogn)
    test(min_array_5) # Segment Trees - Time : O(n) / Query : O(logn) / Space : O(2 * 2^(logN+1))