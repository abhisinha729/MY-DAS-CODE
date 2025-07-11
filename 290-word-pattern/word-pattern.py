class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1={}
        dict2={}
        str_list=s.split()
        if len(pattern)!=len(str_list):
            return False
        for char,word in zip(pattern,str_list):
            if char not in dict1:
                if word in dict2:
                    return False
                else:
                    dict1[char]=word
                    dict2[word]=char
            else:
                if dict1[char]!=word:
                    return False
        return True        


                  