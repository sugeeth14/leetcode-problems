class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        n = len(nums1)
        
        n1 = len(set1)
        n2 = len(set2)
        intersection = set1 & set2
        overlap = len(intersection)
        
        ans = min(min(n1 - overlap, n//2) + min(n2 - overlap, n//2) + overlap, n)
        return ans
        