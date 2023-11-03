class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ans = []
        
        ptr = 0
        
        
        for i in range(1, n + 1):
            if ptr == len(target):
                break
            if i == target[ptr]:
                ans.append("Push")
                ptr += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans
        