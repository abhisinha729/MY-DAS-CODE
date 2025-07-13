class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for char in s:
            if char in dic:
                dic[char]+=1
            else:
                dic[char]=1
        for index,char in enumerate(s):
            if dic[char]==1:
                return index
        return -1                
