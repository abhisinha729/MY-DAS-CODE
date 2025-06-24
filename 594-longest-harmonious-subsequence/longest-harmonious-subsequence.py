class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:  #d{1:1,3:2,2:3,5:1;7:1}
                d[i]=1
            else:
                d[i]+=1  
        result=0         
        for i in d:
            if (i+1 in d and d[i]+d[i+1]>result):
                result=d[i]+d[i+1]
        return result        