class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        section = [set() for _ in range(9)]

        free = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    section[(i//3)*3 + (j//3)].add(board[i][j])
                else:
                    free.append((i,j))


        def is_valid(r,c,num):
            
            if num in rows[r] or num in cols[c]:
                return False
            if num in section[(r//3)*3 + (c//3)]:
                return False
            return True
        
        def sudoku(idx):
            # print(idx)
            if idx == len(free):
                return True

            i,j = free[idx]
            for num in "123456789":
                if is_valid(i,j,num):
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    section[(i//3)*3 + (j//3)].add(num)
                    if sudoku(idx+1):
                        return True
                    rows[i].remove(num)
                    cols[j].remove(num)
                    section[(i//3)*3 + (j//3)].remove(num)
                    board[i][j] = "."
                
            return False
        sudoku(0)