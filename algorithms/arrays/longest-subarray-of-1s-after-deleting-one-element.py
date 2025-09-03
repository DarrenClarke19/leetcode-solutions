'''
Given a binary array nums, delete one element , return the longest non-empty subarray containing only 1s. return 0 if there is no such subarray

Input: nums []
Output : int 

Constraints :
1 <= nums.length <= 10^5
nums[i] is either 0 or 1

Assumptions:
The array isnt empty
All elements are 0 or 1

Test Case: 
[1,1,0,1]

Edge Case: 
[]

Plan/Implement:

Keep at most 1 zero in the window
use pointers left and right for window and increase size using right pointer. if there is a zero increment pointer. 
while zero counter is > 1 increment left and if left element is a 0 decrement zero count
max length is max right-left(this minuses 1 already as we are not including the deleted element)

[0,1,1,1,0,1,1,0,1]
           l 
               r

zero_count=1
max_len=5
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count=0
        left=right=0
        max_len=0
        while right<len(nums):
            if nums[right]==0:
                zero_count+=1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len=max(max_len,right-left)
            right+=1
        return max_len