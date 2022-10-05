class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # if len(s) < 2:
        #     return s
        
        l = 0
        r = len(s)-1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        return s