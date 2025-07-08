class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if haystack==needle:
        #     return 0
        # n=len(haystack)
        # left=0
        # right=len(needle)
        # i=0
        # while (left<n and right<n+1):
        #     sub=haystack[left:right]
        #     if sub==needle:
        #         return i
        #     i+=1    
        #     left+=1
        #     right+=1
        # return -1 
         for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
         return -1          
