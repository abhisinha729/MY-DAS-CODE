class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
       nums.sort()
       p=nums[-1]*nums[-2]*nums[-3]
       q=nums[0]*nums[1]*nums[-1]
       return  max(p,q)
        