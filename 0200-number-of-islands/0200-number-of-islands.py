class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        # Here what we are doing is whenever we find a island what we will do is, we will take DFS on all the direction and will make that island to zero then after we continue the iteration to the grid and if we find another island we will increment the island count and will again do DFS to all the nodes nearby and make it zero

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r,c)

        return island_count