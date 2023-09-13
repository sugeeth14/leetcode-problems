class Solution:
    def candy(self, ratings: List[int]) -> int:
        combined = []
        for i in range(len(ratings)):
            combined.append((ratings[i],i))
        combined.sort()
        # print(combined)
        seen = set()
        ans = [0] * len(ratings)
        for i in range(len(combined)):
            number, index = combined[i]
            current = 1
            if index + 1 in seen:
                if number > ratings[index + 1]:
                    current = ans[index + 1] + 1
            if index - 1 in seen:
                if number > ratings[index - 1]:
                    current = max(current, ans[index-1] + 1)
            ans[index] = current
            seen.add(index)
        return sum(ans)
                
        