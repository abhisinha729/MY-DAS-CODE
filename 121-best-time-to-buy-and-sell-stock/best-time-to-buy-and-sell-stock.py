class Solution:
    #abhi
    def maxProfit(self, prices: List[int]) -> int:
        minPrices=float(inf)
        maxProfit=0
        for i in range(len(prices)):
            if(prices[i]<minPrices):
                minPrices=prices[i]
            elif(prices[i]-minPrices>maxProfit):
                maxProfit=prices[i]-minPrices
        return maxProfit            