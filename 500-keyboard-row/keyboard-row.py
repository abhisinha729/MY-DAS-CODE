class Solution:
    # by using regular expression
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        for i in words:
            if(re.search("^[qwertyuiop]+$",i.lower())) or (re.search("^[asdfghjkl]+$",i.lower())) or(re.search("^[zxcvbnm]+$",
               i.lower())):
               result.append(i)
        return result       
                
