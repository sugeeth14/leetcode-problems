class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted(spells)
        sorted_potions = sorted(potions)
        # print(sorted_spells, spells)
        ans = {}
        ptr1 = 0
        ptr2 = len(sorted_potions) - 1
        while ptr1 < len(sorted_spells) and ptr2 >= 0:
            while sorted_spells[ptr1] * sorted_potions[ptr2] >= success and ptr2 >=0:
                ptr2 -= 1
            ans[sorted_spells[ptr1]] = len(sorted_potions) - 1 - ptr2
            ptr1 += 1
        # print(ans)
        while ptr1 < len(sorted_spells):
            ans[sorted_spells[ptr1]] = len(sorted_potions) - 1 - ptr2
            ptr1 += 1
            
        res = []
        for spell in spells:
            res.append(ans[spell])
        return res
            
                
        