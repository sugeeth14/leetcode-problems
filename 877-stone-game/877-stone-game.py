class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice_score = 0
        bob_score = 0
        
        current_player = 0
        l = 0
        r = len(piles) - 1
        
        while l <= r:
            if current_player % 2 == 0:
                if piles[l + 1] > piles[r - 1]:
                    alice_score += piles[l]
                    l += 1
                elif piles[l + 1] < piles[r - 1]:
                    alice_score += piles[r]
                    r -= 1
                else:
                    if piles[l] >= piles[r]:
                        alice_score += piles[l]
                        l += 1
                    else:
                        alice_score += piles[r]
                        r -= 1
                current_player += 1
            else:
                if piles[l + 1] > piles[r - 1]:
                    bob_score += piles[l]
                    l += 1
                elif piles[l + 1] < piles[r - 1]:
                    bob_score += piles[r]
                    r -= 1
                else:
                    if piles[l] >= piles[r]:
                        bob_score += piles[l]
                        l += 1
                    else:
                        bob_score += piles[r]
                        r -= 1
                current_player += 1
            return alice_score > bob_score
                
        
        