class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        length = len(nums)
        result = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            else:
                l = i + 1
                r = length - 1
                while l < r:
                    threesum = num + nums[l] + nums[r]

                    if threesum > 0:
                        r -= 1
                    elif threesum < 0:
                        l += 1
                    else:
                        result.append([num, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return (result)

                