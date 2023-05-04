class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        R, D = deque(), deque()
        
        for i, char in enumerate(senate):
            if char == "R":
                R.append(i)
            else:
                D.append(i)
                
        while R and D:
            rTop, dTop = R.popleft(), D.popleft()
            if rTop < dTop:
                R.append(rTop + len(senate))
            else:
                D.append(dTop + len(senate))
        
        return "Radiant" if R else "Dire"
        