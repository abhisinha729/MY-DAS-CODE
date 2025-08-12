class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=0
        for char in stones:
            if char in jewels:
                x+=1
        return x