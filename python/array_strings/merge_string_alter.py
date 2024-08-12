"""
Completed: August 10, 2024
Exercise:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str, type word2: str, :rtype: str
        """
        merged_array = []
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            merged_array.append(word1[i])
            merged_array.append(word2[i])

        merged_array.append(word1[min_length:])
        merged_array.append(word2[min_length:])

        return ''.join(merged_array)