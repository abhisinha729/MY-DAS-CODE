class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        dict2={}
        for i  in s:
            if i  in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in t:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
        if dict1!=dict2:
            return False
        else:
            return True                            
        

