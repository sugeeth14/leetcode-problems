class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        
        ptr2 = n - 1
        ptr1 = m - 1
        
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] <= nums2[ptr2]:
                # ptr2 must go at the end
                nums1[last] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[last] = nums1[ptr1]
                ptr1 -= 1
            last -= 1
        
        while ptr1 >= 0:
            nums1[last] = nums1[ptr1]
            last -= 1
            ptr1 -= 1
        while ptr2 >= 0:
            nums1[last] = nums2[ptr2]
            last -= 1
            ptr2 -= 1
        