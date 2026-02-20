class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart,cStart]]
        move = 1
        while len(ans) != rows*cols:
            for _ in range(move):
                cStart += 1
                if 0 <= cStart < cols and 0 <= rStart <rows:
                    ans.append([rStart,cStart])
            for _ in range(move):
                rStart += 1
                if 0 <= cStart < cols and 0 <= rStart <rows:
                    ans.append([rStart,cStart])
            move += 1
            for _ in range(move):
                cStart -= 1
                if 0 <= cStart < cols and 0 <= rStart <rows:
                    ans.append([rStart,cStart])
            for _ in range(move):
                rStart -= 1
                if 0 <= cStart < cols and 0 <= rStart <rows:
                    ans.append([rStart,cStart])
            move += 1
        return ans
