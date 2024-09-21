class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # check if can be placed
                canbeplaced = True
                if i - 1 >= 0:
                    if flowerbed[i-1] == 1:
                        canbeplaced = False
                if i + 1 < len(flowerbed):
                    if flowerbed[i+1] == 1:
                        canbeplaced = False
                if canbeplaced:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
        
        