class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = ""
        counter = 0
        i = 0
        while i < len(s):
            length = len(substring)
            if s[i] not in substring:
                substring += s[i]
                length = len(substring)
                if length > longest:
                    longest = length
                i += 1
            elif s[i] in substring:
                if length > longest:
                    longest = length
                substring = ""
                counter += 1
                i = counter
        return longest
            