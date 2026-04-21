class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ans = []
        rows,cols = len(heights), len(heights[0])
        # top, left, bottom, right = [],[],[],[]
        # for i in range(cols):
        #     top.append([0,i])
        #     bottom.append([cols-1,i])
        # for j in range(rows):
        #     left.append(j,0)
        #     right.append(j, rows-1)
        
        pacific, atlantic = set(), set()

        def dfs(r,c, visit, prev):
            if r <0 or r == rows or c < 0 or c == cols or heights[r][c] < prev or (r,c) in visit:
                return
            visit.add((r,c))

            dfs(r-1,c, visit, heights[r][c])
            dfs(r+1,c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0,c, pacific, heights[0][c])
            dfs(rows-1,c, atlantic, heights[rows-1][c])
        for r in range(rows):
            dfs(r,0, pacific, heights[r][0])
            dfs(r,cols-1, atlantic, heights[r][cols-1])
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    ans.append((i,j))
        
        return ans