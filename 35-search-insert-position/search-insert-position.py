class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        # result=0
        # for i in range(n-1):
        #     if nums[i]==target:
        #         result=i
        #         i+=1
        #     elif nums[i]!=target:
        #         nums.insert(target,i)  
        #         result=i-1
        #         i+=1
               
        # return result
        for i in range(n): #linear search
            if nums[i]>=target:
                return (i)
        return len(nums)        

