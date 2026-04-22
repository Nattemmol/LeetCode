class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols, rows = len(board[0]), len(board)
        visited = set()
        path = list()
        def dfs(r,c):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                return board[r][c] == "X"
            if (r,c) in visited or board[r][c] == "X":
                return True
            
            visited.add((r,c))
            path.append((r,c))

            val = True
            val = val and dfs(r-1, c)
            val = dfs(r+1, c) and val
            
            val = dfs(r, c-1) and val
            val = dfs(r, c+1) and val

            return val

        #dfs(1,1)

        for i in range(1, rows - 1):
            for j in range(1,cols - 1):
                if (i,j) not in visited:
                    
                    path = []
                    is_sur = dfs(i,j)
                    
                    if is_sur:
                        for r,c in path:
                            board[r][c] = "X"
        