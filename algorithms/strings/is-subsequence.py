'''
We want to determine is a string s is a subsequenece of string t; return true or false otherwise. The subsequence should be in the relative order in the string t

Input: s - str, t-str
Output : bool 

Constraints: 
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.

Assumptions: 

Test Case: 
s = "abc", t = "ahbgdc"

Edge Case : 
s="", t=" "

Plan/Implement:

if s is empty return true
j=0
i=0
while i < len(t)
    if t[i]==s[j]
        j+=1
        i+=1
        if j==len(s)-1: return true
    else: 
        i+=1
return false
     

'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        j=0
        i=0
        while i < len(t):
            if t[i]==s[j]:
                j+=1
                i+=1
                if j==len(s): return True
            else: 
                i+=1
        return False
