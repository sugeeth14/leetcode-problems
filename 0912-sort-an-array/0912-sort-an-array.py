class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        
        
        
        
        
        def merge(arr1, arr2):
            ptr1 = 0
            ptr2 = 0
            res = []
            while ptr1 < len(arr1) and ptr2 < len(arr2):
                if arr1[ptr1] < arr2[ptr2]:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    res.append(arr2[ptr2])
                    ptr2 += 1
            while ptr1 < len(arr1):
                res.append(arr1[ptr1])
                ptr1 += 1
            while ptr2 < len(arr2):
                res.append(arr2[ptr2])
                ptr2 += 1
            
            return res
        
        
        
        
        
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            arr1 = merge_sort(arr[:mid])
            arr2 = merge_sort(arr[mid:])
            
            return merge(arr1, arr2)
        return merge_sort(nums)
        