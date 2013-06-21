"""
Given an array of size n, find if there is a number which appears more than n/2 times.

For eg:
A=[1,2,1,1]
Output = 1
A=[1,2,3,4]
Output=None
"""

# The Boyer-Moore Majority Vote Algorithm  I've answered this on stackoverflow before, 
# http://stackoverflow.com/questions/3740371/finding-the-max-repeated-element-in-an-array/3740383#3740383
# The algorithm only works if there exists a majority element. If we don't know, I add an additional linear scan,
# counting the number of times the element appears in the array and verify if it occurs more than n/2 times.

#Complexity : Time: O(n),  Space: O(1)
def majority_algorithm(A):
    currentCount = 0
    currentValue = A[0]
    for val in A:
       if val == currentValue:
          currentCount += 1
       else:
          currentCount -= 1
    
       if currentCount == 0:
          currentValue = val
          currentCount = 1
    
    return currentValue if A.count(currentValue) > len(A)/2 else None

A = [1,2,3]
print A
print majority_algorithm(A)
A = [1,2,1,1]
print A
print majority_algorithm(A)