class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        
        while n not in visit:
            if n==1:
              return True
            visit.add(n)
            n=self.add_square_of_number(n)
        return False
    
    def add_square_of_number(self,n:int) -> int:
        output=0
        while n:
            digit=n%10
            digit=digit**2
            output+=digit
            n=n//10
        return output 
