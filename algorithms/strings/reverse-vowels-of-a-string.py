'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

'''
Given a string we want to reverse only the vowels from opposite ends moving inward. 
Input: s: string
Output s: string

Match: Pointers, strings, arrays

Constraints - length of string is between 1 and 3* 10^5
s is printable ASCII characters

Test Cases: 
s="IcecreAm"

Edge Case = ""

Assumptions : 
Both lower case and upper case 
No need to handle non ascii values
String length is long so solution should be efficient

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            return c.lower() in "aeiou"
        s=list(s)
        i=0 
        j=len(s)-1
        while i<j:
            if not isVowel(s[i]):
                i+=1
            elif not isVowel(s[j]):
                j-=1
            else: 
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)


'''
Another solution without converting to list
class Solution:
  def reverseVowels(self, s: str) -> str:
    def isVowel(char):
      return char.lower() in "aeiou"
      
  vowels = [char for char in s if isVowel(char)]
          result=""
          for char in s:
              if isVowel(char):
                  result+=vowels.pop()
              else:
                  result+=char
          return result
'''
