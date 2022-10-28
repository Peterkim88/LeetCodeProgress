class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        oddExists = False
        
        for v in counts.values():
            
            if oddExists:
                if v % 2 == 0:
                    res += v
                elif v > 2:
                    res += v - 1
            else:
                if v % 2 == 0:
                    res += v
                else:
                    res += v
                    oddExists = True
                
        return res