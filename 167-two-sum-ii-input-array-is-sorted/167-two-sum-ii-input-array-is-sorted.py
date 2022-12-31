class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = [-2000] * 3001



        for i,num in enumerate(numbers):
            a[num + 1000] = i


        indexes = []
        for i, num in enumerate(numbers):
            diff = target - num
            if a[diff + 1000] != -2000:
                indexes = [i + 1, a[diff + 1000] + 1]
                break

        return (indexes)
        