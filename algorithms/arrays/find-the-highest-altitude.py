'''
Given an array gain[] which represents the gain in altitude when a biker starts at point 0 with altitude 0 , find the highest altitude reached.

Input: gain[]
Ouptut: int 

Constraints: 

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

Assumptions: 
Array isnt empty

Plan: 
return max(0,gain[0]) if len(gain)==1
Loop through array from position 2 to position len +1
    find the prefix sum up to position i
    find the max (prefix sum, maxSum)
return 0 if max_sum < 0 else max_sum
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_prefix_sum = max_sum = gain[0]
        if len(gain)==1: return max(0,curr_prefix_sum)
        for i in range(1,len(gain)+1):
            curr_prefix_sum = sum(gain[:i])
            max_sum= max(curr_prefix_sum, max_sum)
        return 0 if max_sum < 0 else max_sum
