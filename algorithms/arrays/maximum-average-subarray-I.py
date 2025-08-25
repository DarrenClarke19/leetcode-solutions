'''
Given an integer array nums , consisting of n elements, and another input integer k , find the suarray with the length=k with the largest average

Input: nums[] , int k
Output : float average

Constraints :
n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4

Assumptions:
array is not empty

Test Case: 
nums = [1,12,-5,-6,50,3], k = 4

Edge Case: 
[5,5,5,5,5]

Plan/Implement:

Match- Sliding Window, Arrays

We could find the current average which is the average of the first k elemenets. change the sum by adding the next element and removing the first till the end of the array

sum = sum(a[:k])
curr = best = sum/k
for i in range(k,len(nums)):
    curr = (sum + nums[i] - nums[k-i]) / k
    best = max(curr,best)
return best


'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_elements = sum(nums[:k])
        curr = best = sum_elements/k
        for i in range ( k, len(nums)):
            sum_elements = sum_elements + nums[i] - nums[i-k]
            curr = sum_elements/k
            best = max(curr,best)
        return best        
