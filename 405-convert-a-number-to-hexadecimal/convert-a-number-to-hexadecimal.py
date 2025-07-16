class Solution:
    def toHex(self, num: int) -> str:
        result=[]
        d={10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        if num==0:
            return "0"
        if num<0:
            num=num+2**32
        while num>0:
            rem=num % 16 # store remainder
            num=num//16    #store quotient
            if rem>=10 :
                result.append(d[rem])
            else:
                rem=str(rem)
                result.append(rem)
        return "".join(result[::-1])    


