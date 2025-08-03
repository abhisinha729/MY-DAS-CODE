class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m=list(moves)

        initial=[0,0]
        
        for x in m:
            if(x=="R"):
                initial[1]+=1
            elif(x=="L"):
                initial[1]-=1
            elif(x=="U"):
                initial[0]-=1
            elif(x=="D"):
                initial[0]+=1
            
        if(initial[0]==0 and initial[1]==0):
            return True
        return False