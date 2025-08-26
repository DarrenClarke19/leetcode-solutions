'''
Given an array chars we want to modify it using a string variable and count the number of
repeating characters and append the character alone to the string variable if that group is 1 otherwise append the character and the count of repeating characters

Input: chars[]
Output: int- count of elements in modified array chars

Constraints: 
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Assumptions:
the array isnt empty

Test Case: 
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Edge Case: 
[]

Implement/Plan
pointer to write to array
i=0
loop till end of array
    count=0
    char = chars[i]
    loop while character is the same
        count++
        i++
    chars[write] = char
    write++
    if count>1
        convert count to string and write each digit
    


'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        write=0
        i=0
        while i < len(chars):
            char = chars[i]
            count=0
            while i < len(chars) and chars[i] == char:
                count+=1
                i+=1
            chars[write]=char
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write

        
