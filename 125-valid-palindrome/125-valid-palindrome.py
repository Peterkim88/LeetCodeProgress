class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        valid = 'abcdefghijklmnopqrstuvwxyz0123456789'
        result = []
        chars = [*s.lower()]
        for c in chars:
            if c in valid:
                result.append(c)
        reverse = result[::-1]
        return result == reverse