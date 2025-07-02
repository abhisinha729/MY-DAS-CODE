class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result=[]
        for i,j in enumerate(operations): # it store key valur paires
            if j=="C":
                result.pop()
            elif j=="D":
                result.append(result[-1]*2)  
            elif j=="+":
                result.append(result[-1]+result[-2])
            else:
                result.append(int(j))    
        return sum(result)        



            

                  