class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        
        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0)
            letters[s[i]] += 1
        
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
            
        return -1