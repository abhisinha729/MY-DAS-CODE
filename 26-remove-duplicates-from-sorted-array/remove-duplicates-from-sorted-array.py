class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        index=1
        if not nums:
            return 0
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[index]=nums[i]
                index+=1
        return index          




        