class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 1
        current = nums[0]
        
        for i in range(1, len(nums)):
            if votes == 0:
                current = nums[i]
                votes = 1
            else:
                if nums[i] == current:
                    votes += 1
                else:
                    votes -= 1
        return current
        