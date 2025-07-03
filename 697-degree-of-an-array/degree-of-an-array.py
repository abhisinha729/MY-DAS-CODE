class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        data = {}
        degree = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            if num not in data:
                data[num] = [1, i, i]  # [count, first_index, last_index] count frequency
            else:
                data[num][0] += 1
                data[num][2] = i

            degree = max(degree, data[num][0])

        for count, first, last in data.values():
            if count == degree:
                min_length = min(min_length, last - first + 1)

        return min_length
