"""
Given an array of N distinct +ve integers and a number S, find the minimum number of elements from the array that sum upto S. You can use an element multiple times.

For eg:
A = [1,2,3,5] and S=17
Output = 5,5,5,2
"""

arr = [5,10,20,25] #tricky test case, greedy won't work.
s = 5

def subset_sum_repeats(arr,s)
  h = Hash.new
  h[0] = [0,-1]
  arr.each {|e|
    h.keys.each{|k|
      i = k;
      c = h[k][0]
      while i+e <= s
        c += 1
        i += e
        h[i] = [c,i-e] if h[i].nil? or c < h[i][0]
      end
        }
    }
  if h[s].nil?
    return nil
  else
    set = []
    while h[s][1] >= 0
      set << (s - h[s][1]) 
      s = h[s][1]
    end
    set
  end
end

p subset_sum_repeats(arr,s)