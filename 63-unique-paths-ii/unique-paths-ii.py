class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        n,m = len(obstacleGrid[0]), len(obstacleGrid)
        unique = [0]* n
        unique[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    unique[j] = 0
                elif j > 0:
                    unique[j] += unique[j-1]
        return unique[-1]