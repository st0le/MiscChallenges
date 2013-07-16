import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

def brute(arr):
    N = len(arr)
    c = 0
    for i in xrange(N):
        for j in xrange(i+1,N):
            if arr[i] > arr[j]:
                c += 1
    return c

def inversions(arr):
    aux = [0] * len(arr)
    def merge_sort(A,lb,ub):
        if ub - lb > 1:
            mid = (lb+ub)/2
            c = merge_sort(A,lb,mid)
            c += merge_sort(A,mid,ub)
            i,j,k = lb,mid,lb
            while i < mid and j < ub:
                if A[i] <= A[j]:
                    aux[k] = A[i]
                    i += 1
                else:
                    aux[k] = A[j]
                    j += 1
                    c += (mid - i)
                k += 1
            while i < mid:
                aux[k] = A[i]
                i += 1
                k += 1
            while j < ub:
                aux[k] = A[j]
                j += 1
                k += 1

            for i in xrange(lb,ub):
                A[i] = aux[i]
            return c
        else:
            return 0
    return merge_sort(arr,0,len(arr))

arr = random_array(10)
print arr
print "Brute Force : ",brute(arr)
print "Merge Sort Variation : ",inversions(arr)