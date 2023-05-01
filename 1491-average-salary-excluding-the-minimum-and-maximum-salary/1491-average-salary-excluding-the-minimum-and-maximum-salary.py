class Solution:
    def average(self, salary: List[int]) -> float:
        sum_needed = sum(salary) - min(salary) - max(salary)
        # return 1/15
        return sum_needed/(len(salary) - 2)