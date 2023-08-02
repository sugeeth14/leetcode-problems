class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permute2(nums, current_length, length, visited, current_list):
            result = []

            if current_length == length:
                result.append(current_list)
                return result

            else:
                for i in range(length):
                    if visited[i]:
                        continue
                    else:
                        visited[i] = True
                        for res in permute2(nums, current_length + 1, length, visited, current_list + [nums[i]]):
                            result.append(res)
                        visited[i] = False
            return result


        visited = [False] * len(nums)

        result = permute2(nums, 0, len(nums), visited, [])
        return (result)