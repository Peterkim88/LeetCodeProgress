# 345. Reverse Vowels of a String
# Easy
# 3.3K
# 2.4K
# company
# Apple
# company
# Bloomberg
# company
# Yahoo
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {"a": True, 
            "e": True, 
            "i": True, 
            "o": True, 
            "u": True, 
            "A": True, 
            "E": True, 
            "I": True, 
            "O": True, 
            "U": True}

        str_vowels = []

        for i in range(len(s)):
            if s[i] in vowels:
                str_vowels.append(s[i])
        
        res = ""

        for c in s:
            if c not in vowels:
                res += c
            else:
                res += str_vowels.pop()

        return res