'''
UNDERSTAND:
Given two strings needle and haystack we want to return the index of the start of the first occurence of needle in haystack and -1 if needle is not present

Input: str haystack, str needle
Output: int index

Constraints: 
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.

Assumptions: 
Strings arent empty
We dont need to convert characters to lower since none are uppercase

Test Case:
haystack = "sadbutsad", needle = "sad"

Edge Case:
haystack = "acwsfsas" , needle = "a"

MATCH:
loop

PROBLEM:

Begin:
    for loop i from 0 to length(haystack)-length(needle)+1:
        if haystack[i:i+length(needle)] == needle then:
            return i 
    return -1
End

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        