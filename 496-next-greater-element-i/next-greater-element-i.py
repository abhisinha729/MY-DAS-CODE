class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        output=[]
        for i in range(len(nums2)):
            ans=-1
            for j in range (i+1,len(nums2)):
                if(nums2[j]>nums2[i]):
                    ans=nums2[j]
                    break
            result.append(ans)    

        dic={nums2[i]:i for i in range(len(nums2))}#dictionary
        for i in nums1:
            index=dic[i]
            output.append(result[index])
        return output                

            