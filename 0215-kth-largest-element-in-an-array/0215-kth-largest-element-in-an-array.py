class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k + 1
        def split_array(sub_array):
            number = sub_array[len(sub_array)//2]
            left_sub_array = []
            right_sub_array = []
            for i in range(len(sub_array)):
                if i == len(sub_array)//2:
                    continue
                    
                if sub_array[i] <= number:
                    left_sub_array.append(sub_array[i])
                else:
                    right_sub_array.append(sub_array[i])
            return left_sub_array, right_sub_array
        
        def find_smallest(current_k, current_sub_array):
            left_sub_array, right_sub_array = split_array(current_sub_array)
            if len(left_sub_array) == current_k - 1:
                return current_sub_array[len(current_sub_array)//2]
            elif len(left_sub_array) > current_k - 1:
                return find_smallest(current_k, left_sub_array)
            else:
                return find_smallest(current_k - len(left_sub_array) - 1, right_sub_array)
        return find_smallest(k, nums)
                
        