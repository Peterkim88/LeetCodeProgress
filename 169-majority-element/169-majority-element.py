class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        
        for n in nums:
            numCount[n] = numCount.get(n, 0)
            numCount[n] += 1
            
        halfLength = len(nums) / 2
        
        for k, v in numCount.items():
            if v > halfLength:
                return k