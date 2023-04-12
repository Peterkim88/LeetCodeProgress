# 266. Palindrome Permutation
# Easy
# 973
# 67
# company
# Facebook
# company
# Google
# company
# Microsoft
# Given a string s, return true if a permutation of the string could form a 
# palindrome
#  and false otherwise.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        counts = {}

        for c in s:
            counts[c] = counts.get(c, 0) + 1

        cnt = 0

        for val in counts.values():
            if val % 2 == 1:
                cnt += 1
            if cnt > 1:
                return False
        
        return True