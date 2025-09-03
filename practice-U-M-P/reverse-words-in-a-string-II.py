'''
UNDERSTAND-
Given a string s and an integer k ,w e must reverse the first k characters of every 2k block of characters, starting from the beginning of the string. If the remaining characters are fewer than k, reverse all of them. If the remaining characters are between k and 2k, reverse the first k, leave the rest unchanged.

Input: str s, int k
Output: str 

Constraints: 
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^4

MATCH-
Python slicing

PROBLEM-

Begin
    Convert s to list of characters (for mutability)
    For i from 0 to len(s) in steps of 2k:
        reverse substring from i to i+k-1 (if within bounds)
    Return the modified string
End

'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)

        for i in range(0, n, 2 * k):
            s[i:i + k] = reversed(s[i:i + k])

        return "".join(s)