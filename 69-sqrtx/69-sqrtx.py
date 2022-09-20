class Solution:
    def mySqrt(self, x: int) -> int:
        squared = False
        root = 0
        while not squared:
            root += 1
            num = root * root
            if num == x:
                squared = True
            elif num > x:
                squared = True
                root -= 1
        
        return root
        