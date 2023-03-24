class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res = []

        low = None

        for i in range(len(nums)):
            if i == len(nums)-1:
                if low == None:
                    res.append(f"{nums[i]}")
                else:
                    res.append(f"{low}->{nums[i]}")
                return res
            
            if low == None:
                low = nums[i]
                
            if nums[i+1]-1 != nums[i]:
                if low == nums[i]:
                    res.append(f"{low}")
                else:
                    res.append(f"{low}->{nums[i]}")
                low = None