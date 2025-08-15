'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

'''
Given an integer array nums ,move all the 0s to the end while maintaining the order of the non zero numbers. Dont return anything
Input: int nums[]

Constraints: 
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Test Case: 
nums = [0,1,0,3,12]

Edge Case : [1,2,3,4,5]

Assumptions: 
The array has at least 1 element
There is at least 1 element that is 0

Plan/Implementation

Use a pointer to keep track of where the next non zero number would go

Loop through array 
    pos=0
    if element is non zero
        num[pos]=non zero element
        pos++
fill the rest of the array with 0s

'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        for i in range(len(nums)): 
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0
