class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x=sorted(score,reverse=True)
        dic={}
        for i in range(len(x)):
            if i==0:
                dic[x[i]]="Gold Medal"
            elif i==1:
                dic[x[i]]="Silver Medal"
            elif i==2:
                dic[x[i]]="Bronze Medal"
            else:
                dic[x[i]]=str(i+1)     
        result=[]
        for i in score:
            result.append(dic[i])     
        return result         


        