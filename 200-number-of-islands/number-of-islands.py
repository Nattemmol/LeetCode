class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        visited = set()
        cols, rows = len(grid[0]), len(grid)
        def dfs(r,c):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                        total += 1
                        dfs(i,j)
        return total
           