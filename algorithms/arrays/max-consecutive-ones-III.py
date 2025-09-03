'''
Given a binary array nums, and an integer k , return the max number of consecutive 1s in the array if you can flip at most k 0s

Input: int nums[]
Output: int

Constraints: 
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length

Assumption :
Array isnt empty
All elements are binary

Test Case: 
[1,1,1,0,0,0,1,1,1,1,0] , k=2

Edge Case :
[1], k=0

Plan/Implement 
2 pointers left and right representing the window 
expand right side to include more numbers and while theres <=k zeroes update the max
if >k zeroes then shrink window from left side until it is valid again.


'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        max_len=0
        zeros=0
        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right+=1
        return max_len