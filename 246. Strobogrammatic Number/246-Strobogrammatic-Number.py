class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        stromb = {
            "0": "0",
            "1": "1",
            "6": "9", 
            "8": "8", 
            "9": "6"
            }

        reversedNum = ""

        for n in num:
            if not n in stromb:
                return False
            reversedNum = stromb[n] + reversedNum

        if num != reversedNum:
            return False
        
        return True