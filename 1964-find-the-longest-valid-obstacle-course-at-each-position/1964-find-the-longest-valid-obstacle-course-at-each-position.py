class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dic = {1: obstacles[0]}
        search_array = [1]
        
        ans = [1] * len(obstacles)
        
        for i in range(1, len(obstacles)):
            # do binary search in the array
            l = 0
            r = len(search_array) - 1
            max_length = 0
            while l <= r:
                mid = (l + r)//2
                length = search_array[mid]
                if dic[length] <= obstacles[i]:
                    max_length = max(max_length, length)
                    l = mid + 1
                else:
                    r = mid - 1
            current_length = max_length + 1
            # print(current_length)
            if current_length in dic:
                dic[current_length] = min(dic[current_length], obstacles[i])
            else:
                dic[current_length] = obstacles[i]
                search_array.append(current_length)
            ans[i] = current_length
        return ans
            
                    
                    
                    
                    
                
        
        