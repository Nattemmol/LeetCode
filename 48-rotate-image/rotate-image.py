class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """   
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r,cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        print(matrix)
        for i in range(rows):
            l = 0
            r = cols-1
            while l < r:
                temp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = temp
                l += 1
                r -= 1

        return matrix