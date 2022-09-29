class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower-1
        
        def formatRange(lower, upper):
            if lower == upper:
                return f"{lower}"
            return f"{lower}->{upper}"
        
        for i in range(len(nums)+1):
            curr = lower
            if i < len(nums):
                curr = nums[i]
            else:
                curr = upper+1
            
            if prev+1 <= curr-1:
                res.append(formatRange(prev+1, curr-1))
            prev = curr
            
        return res