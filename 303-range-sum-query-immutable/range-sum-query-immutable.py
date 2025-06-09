class NumArray:

    def __init__(self, nums: List[int]):
        # initilize the prefix_sum array with a zero at the start
        self.prefix_sum=[0]
        #precompute the prefix sums
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        #calculate the sum of elements from left to right using prefix_sum array
        return self.prefix_sum[right+1]-self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)