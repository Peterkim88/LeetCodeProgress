class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        currPower = 1
        while currPower <= n:
            if currPower == n:
                return True
            currPower = currPower * 3
        
        return False