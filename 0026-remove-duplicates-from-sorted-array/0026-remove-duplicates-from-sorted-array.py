class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Algorithm
        1. Create a set of seen elements
        2. go through current and if current element in seen, continue
        3. Else add the current elemenent to seen
        4. In this case place the current element into last and then incremetn last and current. 
        5. Do this until current reaches the end of nums
        6. Once it reaches, return last.
        """
        
        """
        One for the better space complexity
        """
        if len(nums) < 2:
            return len(nums)
        last = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[last] = nums[i]
                last += 1
        return last
            
        
        
        