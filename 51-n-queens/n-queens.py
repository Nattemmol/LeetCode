class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diagonal = set()
        neg_diagonal = set()
        
        ans = []
        temp = [['.']* n for _ in range(n)]

        def place(r):
            if r == n: 
                ans.append(["".join(tmp[:]) for tmp in temp])
            
            for c in range(n):
                if c in col or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                col.add(c)
                temp[r][c] = 'Q'

                place(r+1)

                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                col.remove(c)
                temp[r][c] = '.'

        place(0)
        return ans


