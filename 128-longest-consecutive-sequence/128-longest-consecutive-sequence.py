class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set()
        edges = {}
        max_length = 0
        
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                # Four cases
                # Case 1: Both are in seen
                if nums[i] - 1 in seen and nums[i] + 1 in seen:
                    edges[nums[i] - 1][1] = edges[nums[i] + 1][1]
                    edges[nums[i] + 1][0] = edges[nums[i] - 1][0]
                    edges[edges[nums[i] - 1][0]][1] = edges[nums[i] + 1][1]
                    edges[edges[nums[i] + 1][1]][0] = edges[nums[i] - 1][0]
                    edges[nums[i]] = edges[nums[i] - 1]
                elif nums[i] - 1 in seen:
                    edges[nums[i] - 1][1] = nums[i]
                    edges[edges[nums[i] - 1][0]][1] = nums[i]
                    edges[nums[i]] = edges[nums[i] - 1]
                elif nums[i] + 1 in seen:
                    edges[nums[i] + 1][0] = nums[i]
                    edges[edges[nums[i] + 1][1]][0] = nums[i]
                    edges[nums[i]] = edges[nums[i] + 1]
                else:
                    edges[nums[i]] = [nums[i], nums[i]]
                
                # print(nums[i])
                # print(edges)
                    
                max_length = max(max_length, edges[nums[i]][1] - edges[nums[i]][0])
                # print(max_length)
        return max_length + 1
                
        