class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        R, D = deque(), deque()
        
        for i, char in enumerate(senate):
            if char == "R":
                R.append(i)
            else:
                D.append(i)
                
        n = len(senate)
                
        while R and D:
            rTop, dTop = R.popleft(), D.popleft()
            if rTop < dTop:
                R.append(rTop + n)
            else:
                D.append(dTop + n)
        
        return "Radiant" if R else "Dire"
        