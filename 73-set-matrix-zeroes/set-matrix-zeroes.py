class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        
        for z in range(len(zeros)):
            row = zeros[z][0]
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for z in range(len(zeros)):
            col = zeros[z][1]
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return matrix
        