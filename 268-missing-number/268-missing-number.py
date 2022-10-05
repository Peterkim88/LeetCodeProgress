class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        high = max(nums)+1
        missingNum = high
        
        for n in range(0, high):
            if n not in nums:
                missingNum = n
                break
            
        return missingNum