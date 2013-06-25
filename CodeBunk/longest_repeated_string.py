"""
Given a string, print the longest repeating substring.
"""

S = "Ask not what your country can do for you, but what you can do for your country".lower()
S = "abbabbbbb"
S = "ababab"

#Kasai Algorithm
#http://math.usm.my/research/onlineproc/cs35.pdf
def build_suffix_array(S):
    N = len(S)
    SA = sorted(xrange(len(S)), key=lambda i:S[i:]) # O(n^2 logn) :(
    Rank = [0] * N
    LCP = [0] * N
    for i in xrange(N):
        Rank[SA[i]] = i
    h = 0
    for i in xrange(N):
        if Rank[i] > 0:
            j = SA[Rank[i] - 1]
            k = max(i,j)
            while k + h < N and S[i+h] == S[j+h]:
                h = h + 1
            LCP[Rank[i]] = h
            if h > 0: h = h - 1
    return (SA,LCP)


#overlap allowed
def longest_common_string(S):
    N = len(S)
    SA,LCP = build_suffix_array(S)
    max_lcp_index = max(xrange(N),key = LCP.__getitem__)
    index = SA[max_lcp_index]
    return S[index:index+LCP[max_lcp_index]]

#non overlapping
def longest_common_string_2(S):
    import heapq
    N = len(S)
    SA,LCP = build_suffix_array(S)
    h = zip(map(lambda n : -n,LCP),xrange(N),SA) #negating the length to make heapq a max-heap
    heapq.heapify(h) #O(n)
    while h:
        lcp,index,sa = heapq.heappop(h)
        lcp = -lcp
        lb = SA[index]
        ub = lb + lcp
        if index - 1 >= 0 and (SA[index-1] + lcp < lb or SA[index-1] >= ub):
            return S[lb:ub]
    return None
    
print "Overlapping allowed : ",longest_common_string(S)
print "Overlapping not allowed : ",longest_common_string_2(S)