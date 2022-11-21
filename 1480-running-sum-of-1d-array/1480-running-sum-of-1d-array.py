class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        rSums = []
        
        for i in range(len(nums)):
            currSum += int(nums[i])
            rSums.append(currSum)
            
        return rSums