'''
UNDERSTAND-
Given a string , convert to lowercase , remove all non alphanumeric characters and if it reads the same forward and backward it is a palindrome

Input: str s
Output: bool

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

Assumptions:
String is not empty

Test Case: "A man, a plan, a canal: Panama

Edge Case: " "

MATCH-

two pointers 

PROBLEM-

Begin 
    s=replace('[^a-zA-Z0-9]',"", str)
    int i = 0 
    int j = len(str)-1
    While i<=j Loop:
        if str[i] != str[j]
            return False
        i++
        j--
    return True
End
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]','', s.lower())
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

