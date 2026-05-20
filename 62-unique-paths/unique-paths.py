class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m
        col = n
        final = [[1]*col for _ in range(row)]

        for i in range(1,row):
            for j in range(1,col):
                final[i][j] = final[i][j-1]+final[i-1][j]
        return final[row-1][col-1]
