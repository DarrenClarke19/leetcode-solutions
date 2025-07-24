# Source : https://leetcode.com/problems/merge-strings-alternately/description/
# Author : Darren Clarke
# Date   : 23/07/2025

"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: word2 is longer, so "rs" is appended at the end.

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: word1 is longer, so "cd" is appended at the end.

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            i += 1
        return "".join(merged)
