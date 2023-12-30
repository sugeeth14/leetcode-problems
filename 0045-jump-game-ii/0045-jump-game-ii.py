class Solution:
    def jump(self, nums: List[int]) -> int:


        first_pointer = 0

        total_steps = 0

        while first_pointer < len(nums) - 1:
            effective_distance = nums[first_pointer] + first_pointer
            if effective_distance >= len(nums) - 1:
                total_steps += 1
                break
            index = first_pointer
            for i in range(1, nums[first_pointer] + 1):
                if i + first_pointer > len(nums) - 1:
                    break
                current_effective_distance = nums[first_pointer + i] + first_pointer + i
                if current_effective_distance > effective_distance:
                    effective_distance = current_effective_distance
                    index = i + first_pointer
            total_steps += 1
            if index == first_pointer:
                first_pointer += nums[first_pointer]
            else:
                first_pointer = index

        return (total_steps)

