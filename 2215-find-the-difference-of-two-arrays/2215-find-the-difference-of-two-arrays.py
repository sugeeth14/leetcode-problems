class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_set1 = set(nums1)
        nums_set2 = set(nums2)
        ans1 = []
        for num in nums_set1:
            if num not in nums_set2:
                ans1.append(num)
        ans2 = []
        for num in nums_set2:
            if num not in nums_set1:
                ans2.append(num)
        
        return [ans1, ans2]
        