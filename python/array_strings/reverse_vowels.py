'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''

# First Attempt at solving the problem
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_placement = []
        word = list(s)

        for letter in s:
            if letter in vowels:
                vowel_placement.append(letter)
        
        for index, letter in enumerate(word):
            if letter in vowels:
                word[index] = vowel_placement.pop()

        return "".join(word)

# Second Attempt at solving the problem after learning two-pointers
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        word = list(s)
        left, right = 0, len(s) -1

        while left < right:
            if word[left] not in vowels:
                left += 1
            elif word[right] not in vowels:
                right -= 1
            else:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
        return ''.join(word)