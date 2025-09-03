'''
UNDERSTAND:
Given an input string as a list of characters , reverse the string  by modifying the input array in place

Input: char s[]
Output : no return

Constraints: 
1 <= s.length <= 10^5
s[i] is a printable ascii character.

Assumptions:
list is not empty

Test Case: s = ["h","e","l","l","o"]

Edge Case: [" "]

MATCH-

2 pointers

PROBLEM-
Begin 
    int i=0
    int j=length(s)-1
    While i<j Loop:
        temp = s[i]
        s[i]=s[j]
        s[j]=temp
        i++
        j--
End
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
            