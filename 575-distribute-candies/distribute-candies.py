class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        #s={1,2,3}=3 and length of s=6/2=3  here we are returning minimum value between size of set and size of s
        #s={1,2,3}=3 and lenght of s=4/2=2
        #s={6}=1 and length of s=4/2=2
        s=set(candyType)
        size=len(s)
        x=int(len(candyType)/2)
        # for i in range(x):
        #     if size>=x and size>=x:
        #         return x 
        return (min(x,size)) 
