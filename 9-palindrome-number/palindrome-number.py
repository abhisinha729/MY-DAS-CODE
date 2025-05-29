class Solution:
    #abhi
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        xcopy=x
        tempo=0
        while x>0:
            tempo=(10*tempo)+(x%10)
            x=x//10
        return tempo==xcopy        


        