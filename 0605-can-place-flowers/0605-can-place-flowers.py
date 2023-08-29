class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                count = 0
                if i - 1 < 0 or flowerbed[i-1] == 0:
                    count += 1
                if i + 1 == len(flowerbed) or flowerbed[i+1] == 0:
                    count += 1
                if count == 2:
                    n -= 1
                    flowerbed[i] = 1
        if n>0:
            return False
        return True
                
                
        