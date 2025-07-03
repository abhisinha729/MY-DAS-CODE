class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        index=1#pointer
        count=0
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                count=0
                nums[index]=nums[i]
                index+=1
            else:
                count+=1
                if count<=1:
                    nums[index]=nums[i]
                    index+=1
        return index            



