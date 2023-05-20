class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def merge(array1, array2):
            ans = []
            ptr1 = 0
            ptr2 = 0
            while ptr1 < len(array1) and ptr2 < len(array2):
                if array1[ptr1] < array2[ptr2]:
                    ans.append(array1[ptr1])
                    ptr1 += 1
                else:
                    ans.append(array2[ptr2])
                    ptr2 += 1
            while ptr1 < len(array1):
                ans.append(array1[ptr1])
                ptr1 += 1
            while ptr2 < len(array2):
                ans.append(array2[ptr2])
                ptr2 += 1
            return ans
        
        def merge_sort(array):
            if len(array) == 1:
                return array
            else:
                mid = len(array)//2
                array1 = merge_sort(array[:mid])
                array2 = merge_sort(array[mid:])
                
                merged_array = merge(array1, array2)
                return merged_array
        
        res = merge_sort(nums)
        return res
            
        
        