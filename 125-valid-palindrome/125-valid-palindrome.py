class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        chars = [*s.lower()]
        result = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for char in chars:
            if char in alphabet:
                result.append(char)
        # print(result)
        reversed = result[::-1]
        return result == reversed
        # print(chars)