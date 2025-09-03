'''
Given an integer array nums , find the index such that the sum of elements to the right and left are equal

Input: int nums[]
Output: int

Constraints:
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

Assumptions: 

Test Case:

nums = [1,7,3,6,5,6]

Edge Case:
[-1-1,2,2] No pivot index

Plan/Implement

Find the total sum
Keep track of left sum and check on each iteration if left sum is equal to write sum
return i 
return -1 otherwise

'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i, num in enumerate(nums):
            if left_sum==total-left_sum-num:
                return i
            left_sum+=num
        return -1
