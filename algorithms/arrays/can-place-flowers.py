'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

'''
Given an integer array containing 0s and 1s where 0 is empty and 1 is not empty and given an integer n which is the number of flowers we want to "plant" in the empty locations without planting adjacent flowers

Input : int array flowerbed[]
Output : bool

Constraints : 
flowerbed length is between 1 and 2*10^4
each index is 0 or 1
No two adjacent flowers in flowerbed
n is between 0 and length of flowerbed

Assumptions: 
Length of flowerbed is large so we need an efficient solution

Test Cases: 
flowerbed =[1,0,0,0,1], n = 1
Output: true

Edge Case = [] n=1

Implement:

Loop through flowerbed:
    if the current flower pot is empty 
        check that the right and left of that location is also empty 
            if both empty 
                plant at that location 
                decrement n
                check if n is 0, if true return true
return n==0
            
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List
         for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n == 0
