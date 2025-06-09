class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # lis=[]
        # count=0
        # for i in nums:
        #     if i==0:
        #         count+=1
        #     else:
        #         lis.append(i)
        # for i in range (count):
        #     lis.append(0)
        # for i in range(len(lis)):
        #     nums[i]=lis[i]
        # return nums    
        i,j=0,0
        while(j<len(nums)):
             if (nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
             j+=1 
        return nums       


