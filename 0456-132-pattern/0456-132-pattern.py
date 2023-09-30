from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        smallest = []
        smallest.append(float(inf))
        
        current_smallest = nums[0]
        for i in range(1,len(nums)):
            smallest.append(current_smallest)
            current_smallest = min(nums[i], current_smallest)
        # print(smallest)
        # on the right we have to find the largest less than current numbers
        right = SortedList()
        
        for i in range(len(nums)-1,-1,-1):
            index = right.bisect_left(nums[i])
            if index != 0:
                if right[index-1] > smallest[i]:
                    return True
            right.add(nums[i])
        return False
            
        