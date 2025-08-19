class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        s=""; di={}
        for i in paragraph:
            if(i not in ("!?',;. ")):
                s=s+i
            else:
                if((s not in banned) and s!=""):
                    if(s in di.keys()):
                        di[s]+=1
                    else:
                        di.setdefault(s,1)
                s=""
        maxv,maxk=0,s
        for key,value in di.items():
            if(value>maxv):
                maxv=value; maxk=key
        return maxk