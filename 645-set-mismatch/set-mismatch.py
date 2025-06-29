class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result=[]
        if nums[0]==0:
            return False
        nums.sort()   
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                result.append(nums[i])
                      

        fullset=set(range(1,len(nums)+1)) #(1,5) [1,2,2,4]
        numset=set(nums)#{1,2,4}
        missing_value=list(fullset-numset)[0]
        result.append(missing_value)
        return result

        #  full_set = set(range(1, len(nums) + 1))
        # num_set = set(nums)
        # missing = list(full_set - num_set)[0]
        # result.append(missing)