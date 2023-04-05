# 258. Add Digits
# Easy
# 3.3K
# 1.8K
# company
# Amazon
# company
# Apple
# company
# Bloomberg
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1
 

# Follow up: Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num: int) -> int:
        prevNums = str(num)

        while len(prevNums) > 1:
            subRes = "0"

            for n in prevNums:
                subTotal = int(subRes) + int(n)
                subRes = str(subTotal)
            
            prevNums = subRes

        return int(prevNums)
