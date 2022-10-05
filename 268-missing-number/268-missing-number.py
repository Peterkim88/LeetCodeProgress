class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        high = max(nums)+1
        
        for n in range(0, high):
            if n not in nums:
                return n
            
        return high