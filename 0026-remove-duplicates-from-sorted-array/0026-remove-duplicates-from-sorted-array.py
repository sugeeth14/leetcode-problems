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
        last = 0
        current = 0
        
        seen = set()
        for current in range(len(nums)):
            if nums[current] in seen:
                continue
            else:
                seen.add(nums[current])
                nums[last] = nums[current]
                last += 1
                current += 1
        return last
        
        