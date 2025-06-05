class Solution:
    #abhi
    def singleNumber(self, nums: List[int]) -> int:
        resultDic={}
        for i in nums:
            if(i not in resultDic.keys()):# return only keys
                resultDic[i]=1
            else:
                resultDic[i]+=1
        for i in resultDic:
            if (resultDic[i]==1):
                return i       
            
        