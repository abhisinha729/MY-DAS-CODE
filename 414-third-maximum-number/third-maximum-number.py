class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #abhi
        # nums=set(nums)
        # if len(nums)<3:
        #     return max(nums)
        # nums.remove(max(nums))
        # nums.remove(max(nums))
        # return max(nums) 
        nums=list(set(nums))   
        nums.sort()
        if len(nums)<=2:
            return nums[-1]
        else:
            return nums[-3]    
