class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        visited = set()
        
        visited.add(0)
        queue = collections.deque()
        queue.append((0, 0))
        
        while queue:
            top, steps = queue.popleft()
            if top == len(nums) - 1:
                return steps
            else:
                for i in range(nums[top]):
                    next_index = top + i + 1
                    if next_index not in visited and next_index < len(nums):
                        visited.add(next_index)
                        queue.append((next_index, steps + 1))
            # print(queue)
        
            
        
        