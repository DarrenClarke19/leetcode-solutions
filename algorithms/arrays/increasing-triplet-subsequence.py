'''
Given an integer array nums return true if there is a triple of indices (i,j,k) such that i<j<k and nums[i] < nums[j] < nums[k] and false if no such indices exist.

Input : integer nums[]
Output : bool

Constraints : 
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Test Case : 
nums = [5,4,3,2,1]

Edge Case:
[]

Assumptions: 
The array has at least 1 element
There are positive and negative elements

Match: Arrays

Implement:
Loop through array
Keep track of smallest number and second smallest
Update smallest and second smallest until we find a number bigger than our second smallest.
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=float('inf')
        second=float('inf')
        for num in nums:
            if num < first:
                first=num
            elif num>first and num<second:
                second=num
            elif num>second:
                return True
        return False
            
