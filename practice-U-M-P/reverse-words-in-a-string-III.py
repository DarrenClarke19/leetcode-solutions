'''
UNDERSTAND-
Given a string , reverse the characters of each word, preserving whitespace and word order

Input: str s
Output: str s

Constraints: 
1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.


Test Case: s = "Let's take LeetCode contest"

Edge Case: s=" Mr Ding"

MATCH-

Split + reverse

PROBLEM-
Begin
    split string s into words
    for each word in words:
        reverse the word
    join reversed words with a single space
    return result
End

'''