class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result=[]
        # for num in nums1:
        #     if(num in nums2 and num not in result):
        #         result.append(num)
        # return result        
        nums3=set(nums1)
        nums4=set(nums2)
        result=list(nums3 & nums4)
        return result  
