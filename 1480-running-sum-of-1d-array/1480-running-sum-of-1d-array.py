class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = {}
        for i in range(len(nums)):
            runningSum[i] = runningSum.get(i, nums[i])
            if i-1 in runningSum:
                runningSum[i] += runningSum[i-1]
        return runningSum.values()