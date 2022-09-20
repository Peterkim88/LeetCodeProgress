class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        nums = digits[::-1]
        
        for i in range(len(nums)):
            n = nums[i]
            if carry == True:
                if n == 9:
                    nums[i] = 0
                    carry = True
                else:
                    nums[i] = n + 1
                    carry = False
        if carry:
            nums.append(1)
            
        return nums[::-1]