'''
Find the max area where each index represents x axis value and its value represents y axis value

Input: int height[]

Ouput: int

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 10^4

Assumptions: 
height array has at least 2 values
a height can be 0

Test Case:
height = [1,8,6,2,5,4,8,3,7]

Edge Case: 
[0,1]

Plan/Implement:

Find the area of opposite ends. The area is calculated using the minimum of the heights by the length (rght index - left index)
Since the smaller height is the limiting factor we should move to the index next to the smaller of the two

left = 0
right = len(height)-1
max_area=0
    while left<right:
        area=(right-left)*(min(height[left],height[right]))
        max_area=max(max_area,area)
        if height[left]>height[right]:
            right-=1
        else:
            left+=1
    return max_area

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right= 0, len(height)-1
        max_area=0
        while left<right:
            area=(right-left)*(min(height[left],height[right]))
            max_area=max(max_area,area)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_area

