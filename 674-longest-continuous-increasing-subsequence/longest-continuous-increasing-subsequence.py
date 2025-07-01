class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result=0
        n=len(nums)
        if  not  nums: #check if list is empty or not
            return 0
        max_len=1
        curr_len=0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                max_len=max(max_len,i-curr_len+1) #window continue
            else:
                curr_len=i
        return max_len            
       
