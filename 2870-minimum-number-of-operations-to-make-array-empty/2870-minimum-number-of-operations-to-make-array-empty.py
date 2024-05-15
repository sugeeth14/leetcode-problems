class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        Algorithm:
        1. Keep a count of frequencies of each element in the array.
        2. Iterate through the count, if the count is 1 return -1.
        3. Else, check the mod by 3 for the count.
        4. If mod is zero divide the count by 3 and add it to the res.
        5. If the mod is 2, lower divide the count and add 1 to it.
        6. If the mod is 1, subtract 4 from it and divide by 3 and add to the res and add 2 to the res to include for the 4.
        '''
        res = 0
        
        dic = collections.defaultdict(int)
        
        for num in nums:
            dic[num] += 1
        
        for num in dic:
            if dic[num] == 1:
                return -1
            else:
                count = dic[num]
                remainder = count % 3
                if remainder == 0:
                    res = res + (count // 3)
                elif remainder == 2:
                    res = res + (count // 3) + 1
                else:
                    count -= 4
                    res = res + (count // 3) + 2
        return res
        