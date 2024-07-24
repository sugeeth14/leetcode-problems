class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        mapping_dic = {}
        for i in range(len(mapping)):
            mapping_dic[str(i)] = str(mapping[i])
        
        dic = {}
        
        
        def get_num(num):
            num = str(num)
            
            ans = ""
            for char in num:
                ans += mapping_dic[char]
            
            return int(ans)
        for num in nums:
            dic[num] = get_num(num)
        
        # print(dic)
        return sorted(nums, key=lambda x: dic[x])