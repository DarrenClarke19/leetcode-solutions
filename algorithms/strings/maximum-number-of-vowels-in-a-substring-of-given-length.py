'''
Given a string s and an integer k , return the maximum number of vowel letters in any substring of s with length k

Input: str s, int k
Output: int 

Constraints :
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Assumptions: 

String is not empty
IsVowel method doesnt convert characters to lowercase since there are no uppercase letters

Match : 
Sliding Window , strings, two pointers

Plan/Implement:

Sliding Window. Check if the first k elements are vowels and find the count of that. That is the current max number of vowels in a substring. Loop from k to n-1 and check if that element is a vowel. That element is the element entering the window but if the i-k element is also a vowel then we minus it from the count since that element is leaving the window



'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(char):
            return char in "aeiou"
        
        curr = sum(1 for char in s[:k] if isVowel(char))
        best = curr
        for i in range(k,len(s)):
            if isVowel(s[i]):
                curr += 1
            if isVowel(s[i-k]):
                curr -= 1
            best = max(best, curr)
        return best
        
            
        
