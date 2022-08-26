class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}
        for char in s:
            if not char in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
        for char in t:
            if not char in letter_count:
                return False
            else:
                letter_count[char] -= 1
        for v in letter_count.values():
            if not v == 0:
                return False
        return True