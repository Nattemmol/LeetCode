class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique = [[1] * n for _ in range(m)]
        
        print(unique)
        for i in range(1,m):
            for j in range(1,n):
                print(i,j)
                unique[i][j] = unique[i-1][j]+unique[i][j-1]
        
        return unique[m-1][n-1]
                

