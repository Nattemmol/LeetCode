class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        print(mat)
        for _ in range(4):
            for i in range(len(mat)):
                for j in range(i,len(mat[0])):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
            for i in range(len(mat)):
                l = 0
                r = len(mat[0])-1
                while l < r:
                    mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                    l += 1
                    r -= 1
            if mat == target:
                return True
        return False