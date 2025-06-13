class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count=0
        if (len(grid)==0):
            return 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=self.AdjacentSide(grid,i,j)
        return count

    def AdjacentSide(self,grid:[List[int]],i:int,j:int):
        pick=0
        cells=[(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
        for x,y in cells:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                pick+=1
        return pick                    