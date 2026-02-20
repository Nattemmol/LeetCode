class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        up = True
        ans = []
        cur_col = 0
        cur_row = 0
        while len(ans) != row * col:
            if up:
                while cur_row >=0 and cur_col < col:
                    ans.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == col:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                up = False
            else:
                while cur_col >= 0 and cur_row < row:
                    ans.append(mat[cur_row][cur_col])
                    cur_col -= 1
                    cur_row += 1
                if cur_row == row:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                up = True
        return ans
        