class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target == n:
                return i
        return -1