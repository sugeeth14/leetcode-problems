class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            current_number = nums[i]
            if current_number - 1 == i:
                continue
            if current_number == nums[current_number - 1]:
                return current_number
            # Else we must place the number in its correct location
            while True:
                location = current_number - 1
                if nums[location] == current_number:
                    break
                else:
                    current_number, nums[location] = nums[location], current_number
                    nums[i] = current_number
            if nums[i]-1 != i:
                return nums[i]
            
        # print(nums)           
        # print("came here")      
            
        