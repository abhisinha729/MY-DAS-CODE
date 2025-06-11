class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        nums=set(nums)
        for num in range(1,n+1):
            if(num not in nums):
                result.append(num)
        return result        
        