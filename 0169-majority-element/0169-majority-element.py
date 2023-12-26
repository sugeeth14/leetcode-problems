class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Algorithm:
        1. We will be doing boore moyre voting algorithm approach
        2. We will start with first element and the number of votes it received as 1
        3. If we encounter a different element, we reduce the number of votes of the current element
        4. If the number of votes is already 0, we replace the current element with the new element and make its vote as 1
        5. At the end, the element left behind in the current variable would be the majority element.
        """
        
        current = nums[0]
        
        votes = 1
        
        for i in range(1, len(nums)):
            if nums[i] != current:
                if votes == 0:
                    current = nums[i]
                    votes = 1
                else:
                    votes -= 1
            else:
                votes += 1
        return current
        