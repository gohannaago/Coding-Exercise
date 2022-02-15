""" 
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of 
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initiate counter for islands
        counter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    counter+=1
        return counter
        
    
    # DFS function to mark visited vertices
    def dfs(self,grid,i,j):
        # mark current vertex visited
        grid[i][j] = "v"
        # do dfs for adjacent vertex
        if i > 0 and grid[i-1][j] == "1":
            self.dfs(grid,i-1,j)
        if i < len(grid)-1 and grid[i+1][j] == "1":
            self.dfs(grid,i+1,j)
        if j > 0 and grid[i][j-1] == "1":
            self.dfs(grid,i,j-1)
        if j < len(grid[0])-1 and grid[i][j+1] == "1":
            self.dfs(grid,i,j+1)