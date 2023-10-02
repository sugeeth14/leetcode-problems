class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice_moves = 0
        current = 0
        for i in range(len(colors)):
            if colors[i] == "A":
                current += 1
            else:
                alice_moves += max(current - 2, 0)
                current = 0
        
        alice_moves += max(current - 2, 0)
        
        current = 0
        bob_moves = 0
        for i in range(len(colors)):
            if colors[i] == "B":
                current += 1
            else:
                bob_moves += max(current -2, 0)
                current = 0
        bob_moves += max(current-2,0)
        
        return alice_moves > bob_moves
        
        