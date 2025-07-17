class Solution:
    def longestPalindrome(self, s: str) -> int:
        lenght=0
        dic={}
        for char in s:
            if char not in dic:
                dic[char]=1
            else:
                dic[char]+=1
        for k,v in dic.items():
            lenght+=v//2*2
            if(lenght%2==0 and v%2==1):
                lenght+=1
        return lenght        