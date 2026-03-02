class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum_arr = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.sum_arr[i][j] = self.sum_arr[i][j-1] + self.sum_arr[i-1][j] - self.sum_arr[i-1][j-1]+matrix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2 = row1+1,row2+1,col1+1,col2+1
        result = self.sum_arr[r2][c2] - self.sum_arr[r2][c1-1] - self.sum_arr[r1-1][c2] + self.sum_arr[r1-1][c1-1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)