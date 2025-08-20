'''
Reverse the words in a string separated by " " . if there is multiple spaces remove multiple spaces or leading and trailing spaces

Input : s : str
Output : str

Constraint: 
Length of string is 1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Test Cases :
Input: s = "  hello world  "

Edge Case: s= "a"

Plan :
start from the end of the string and loop backward
if char is not " " then append that to a word list 
if word is not empty then reverse the word list and join it wiht no spaces and add it to the result list. then set word list to empty 
if word is non empty add it to result
return result joined by " " 


'''
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        wordList=s.split()
        return " ".join(wordList[::-1])

        '''

        '''
        i=len(s)-1
        result=[]
        while i>=0:
            while i>=0 and s[i] == " ":
                i-=1
            if i<0:
                break
            j=i
            while i>=0 and s[i]==" ":
                i-=1
            result.append(s[i+1:j+1])
        return " ".join(result)
        '''

        i=len(s)-1
        result=[]
        word=[]
        while i>=0:
            if s[i]!=" ":
                word.append(s[i])
            elif word:
                result.append("".join(reversed(word)))
                word=[]
            i-=1
        if word:
            result.append("".join(reversed(word)))
        return " ".join(result)
