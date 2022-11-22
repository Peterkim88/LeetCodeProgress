class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numSum = sum(nums)
        leftsum = 0
        
        for i, n in enumerate(nums):
            if leftsum == (numSum - leftsum - n):
                return i
            leftsum += n
        
        return -1