class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        '''
        Algorithm:
        1. This is a two pass algorithm
        2. In first pass, start from the left and get the minimum element and its left most index.
        3. In the second pass, start from the right and get the maximum element and its right most index.
        4. If left min and right max are not intersected, return the distances of two extremes as a sum.
        5. If they have an overlap, return sum of distances - 1
        '''
        max_value = max(nums)
        min_value = min(nums)
        
        min_index = -1
        for i in range(len(nums)):
            if nums[i] == min_value:
                min_index = i
                break
        
        max_index = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == max_value:
                max_index = i
                break
        #check for overlap
        if max_index >= min_index:
            return len(nums) - 1 - max_index + min_index
        else:
            return len(nums) - 1 - max_index + min_index - 1
        