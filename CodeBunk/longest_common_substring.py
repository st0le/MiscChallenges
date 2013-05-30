"""
Give 2 strings, find the longest common substring.

For eg:
A = 'aabbab'
B = 'ccbbad'
Output = 'bba'
"""

A = 'hi, my name is gaurav'
B = 'hi gaurav, my name is foobar.'

def longest_common_substring(A,B):
  L = [[0] * len(B) for i in xrange(len(A))]
  z = 0
  ret = set()
  for i in xrange(len(A)):
    for j in xrange(len(B)):
      if A[i] == B[j]:
        L[i][j] = 1 if i*j == 0 else L[i-1][j-1] + 1
        if L[i][j] > z: #new longer common subtring?
          z = L[i][j]
          ret = {A[i-z+1:i+1]}
       	if L[i][j] == z:
          ret.add(A[i-z+1:i+1])
      else:
        L[i][j] = 0
  return ret

print longest_common_substring(A,B)