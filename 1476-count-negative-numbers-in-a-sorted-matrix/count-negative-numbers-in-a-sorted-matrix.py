class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][-1] >= 0:
                    break
                if grid[i][j] < 0:
                    count += len(grid[i][j:])
                    break
        return count

