class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        return evens + odds
        