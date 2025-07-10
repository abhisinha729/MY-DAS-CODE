class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        dict2={}
        for i,j in zip(s,t): #zip is use to combine multiple values
            if i in dict1 and dict1[i]!=j:
                return False
            if j in dict2 and dict2[j]!=i:
                return False
            dict1[i]=j
            dict2[j]=i
        return True        


