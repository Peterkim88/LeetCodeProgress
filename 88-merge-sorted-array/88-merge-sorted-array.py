class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # l = len(nums1)-1
        # for i in range(len(nums2)-1, -1, -1):
        #     nums1[l] = nums2[i]
        #     l -= 1
        # return nums1.sort()
        last = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
            
        return nums1