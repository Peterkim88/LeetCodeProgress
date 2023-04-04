# 119. Pascal's Triangle II
# Easy
# 3.7K
# 297
# company
# Amazon
# company
# Yahoo
# company
# Goldman Sachs
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        i = 1
        prev = [1,1]
        res = []

        while i < rowIndex:
            res.append(1)
            for j in range(len(prev)-1):
                res.append(prev[j] + (prev[j+1]))
            res.append(1)
            
            i += 1
            prev = res
            res = []

        return prev