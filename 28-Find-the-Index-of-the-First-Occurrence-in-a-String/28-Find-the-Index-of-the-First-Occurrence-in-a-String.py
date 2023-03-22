class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)

        for i in range(len(haystack)):
            j = i + needleLength
            substr = haystack[i:j]
            if substr == needle:
                return i
        
        return -1