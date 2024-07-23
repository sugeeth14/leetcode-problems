class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        
        
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        # print(dic)
        
        def custom_sort(item):
            return (dic[item], -item)
        
        ans = []
        for val in sorted(dic, key=custom_sort):
            ans = ans + [val] * dic[val]
        return ans
        