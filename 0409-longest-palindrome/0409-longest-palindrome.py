class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        
        for count in counts.values():
            res += count // 2 * 2
            if res % 2 == 0 and count % 2 != 0:
                res += 1
                
        return res
#         counts = Counter(s)
#         res = 0
#         oddExists = False
        
#         for v in counts.values():
            
#             if oddExists:
#                 if v % 2 == 0:
#                     res += v
#                 elif v > 2:
#                     res += v - 1
#             else:
#                 if v % 2 == 0:
#                     res += v
#                 else:
#                     res += v
#                     oddExists = True
                
#         return res