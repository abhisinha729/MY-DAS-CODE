class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        d={}
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
        for char in t :
            if char not in d or d[char]==0:
                return char
            else:
                d[char]-=1    
