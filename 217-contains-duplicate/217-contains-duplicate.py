class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for n in nums:
            if n in numbers:
                return True
            numbers[n] = True
        return False
        