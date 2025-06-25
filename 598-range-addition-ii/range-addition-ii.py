class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        maxCol, minCol=m,n
        for i,j in ops:
            maxCol=min(maxCol,i)
            minCol=min(minCol,j)
        return maxCol*minCol