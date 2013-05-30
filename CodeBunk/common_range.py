#Bunk has a problem:
#
#A range is defined as (a,b) which means all numbers between a and b inclusive. Assume a,b to be integers.
#
#Given a list of ranges, find the common range.
#
#For eg:
#[(1,5), (4,9), (3,7)]
#Output = (4,5)



def commonRange(I):
  start,end = reduce(lambda (a,b),(c,d) : (max(a,c),min(b,d)) , I)
  return None if start > end else (start,end)



t = [(1,5), (4,9), (3,7), (4,10)]
print commonRange(t)

I = [(28, 60), (14, 50), (11, 38), (20, 70), (17, 30)]
print commonRange(I)