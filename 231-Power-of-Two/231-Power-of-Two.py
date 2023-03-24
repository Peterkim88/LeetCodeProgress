class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        curr = 2

        if n == 1:
            return True
        
        while curr <= n:
            if curr == n:
                return True
            curr *= 2
        
        return False