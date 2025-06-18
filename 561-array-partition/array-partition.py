class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        x=sorted(nums)
        max=0
        for i in range(0,len(x),2):
            max+=x[i]
        return max    

        