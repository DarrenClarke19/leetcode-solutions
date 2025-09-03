'''
Given  two int arrays, return a list answer of size 2 where answer[0] is a list of distinct integers in nums1 but not in nums2 and answer[1] is a list of distinct integers in num2 but not in nums1

Input: int nums1[] , int nums2[]
Output: answer[]

Constraints: 
1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000

Match: 
sets- sets have methods to find the difference between two sets

Plan/Implement:
convert lists to sets
find differenc of both
convert back to list and return in a list

'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1_set,nums2_set=set(nums1),set(nums2)

        only_in_nums1=nums1_set.difference(nums2_set)
        only_in_nums2=nums2_set.difference(nums1_set)

        return [list(only_in_nums1),list(only_in_nums2)]