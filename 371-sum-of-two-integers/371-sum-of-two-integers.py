class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        while a > 0:
            res += 1
            a -= 1
        while b > 0:
            res += 1
            b -= 1
        while a < 0:
            a += 1
            res -= 1
        while b < 0:
            b += 1
            res -= 1
            
        return res