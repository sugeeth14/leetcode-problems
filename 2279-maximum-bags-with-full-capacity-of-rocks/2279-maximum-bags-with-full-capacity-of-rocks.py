class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        difference_array = []
        for i in range(len(capacity)):
            difference_array.append(capacity[i] - rocks[i])
        difference_array.sort()
        count = 0
        for i in range(len(difference_array)):
            additionalRocks -= difference_array[i]
            if additionalRocks >= 0:
                count += 1
        return count
        