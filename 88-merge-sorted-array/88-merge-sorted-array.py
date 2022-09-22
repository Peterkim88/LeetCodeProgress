class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         l = 0
#         r = 0
#         tmp = nums1[l]
#         while l <= len(nums1):
#             subtemp = nums1[l]
#             nums1[l] = tmp
#             if r < len(nums2) and nums2[r] < nums1[l] and nums2[r] < subtemp:
                
                
#                 subtemp = nums1[l]
#                 nums1[l] = tmp
#                 tmp = subtemp
#             else:
#                 tmp = nums1[l]
#                 nums1[l] = nums2[r]
#                 r += 1
#             l += 1
#         return nums1
        l = len(nums1)-1
        for i in range(len(nums2)-1, -1, -1):
            nums1[l] = nums2[i]
            l -= 1
        return nums1.sort()