class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
#         for i in range(len(nums)):
#             if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
#                 return i           
#         return -1
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        
        return -1