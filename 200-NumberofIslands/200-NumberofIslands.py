# Last updated: 11/5/2025, 2:19:41 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows= len(grid)
        num_cols= len(grid[0])
        island_count = 0

        def dfs(row: int, col: int) -> None:
            if row < 0 or row>= num_rows or col<0 or col >= num_cols:
                return
            
            if grid[row][col]=='0':
                return
            
            grid[row][col]='0'

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col]=='1':
                    dfs(row, col)
                    island_count +=1
        return island_count

