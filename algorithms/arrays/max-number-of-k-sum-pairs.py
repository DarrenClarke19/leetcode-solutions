'''
Given an integer array nums and an integer k , count how many times a pair of numbers sum equals k and remove them from the array, return the count 

Input: 
int [] , int

Output : int 

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9

Assumptions: 
array isnt empty
positive elements only

Test Case: 
[1,2,3,4], k = 5

Edge Case:
nums = [1, 2, 3], k = 10

nums = [1, 1, 1, 1], k = 2

Match: 2 pointer

Plan/Implement:
Sort the array
Two pointers for left and right of array
while left<right
    if left ele + right ele == k
        increment count , both pointers
    else if left ele + right ele <k:
        left ++
    else: 
        right --
return count

'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left , right = 0 , len(nums)-1 
        count=0
        while left<right:
            if nums[left] + nums[right] == k:
                count+=1
                left+=1
                right-=1
            elif nums[left] + nums[right] < k:
                left +=1
            else:
                right-=1
        return count
