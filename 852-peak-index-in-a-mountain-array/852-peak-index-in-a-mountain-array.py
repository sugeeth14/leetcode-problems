class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r)//2
            # print(arr[mid])
            if arr[mid-1] < arr[mid] > arr[mid + 1]:
                return mid
            else:
                # it can be part of increasing or decreasing mountain
                if arr[mid-1] < arr[mid]:
                    l = mid
                else:
                    r = mid
        return mid
        
        