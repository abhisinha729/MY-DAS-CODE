class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result=0
        for i in range(k):
            result+=nums[i]
        max_Sum=result

        start_index=0
        end_index=k
        while(end_index<len(nums)):
            result-=nums[start_index]
            start_index+=1

            result+=nums[end_index]
            end_index+=1
            max_Sum=max(max_Sum,result)
        return(max_Sum/k)   



