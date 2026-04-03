# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.moves = 0

        def dfs(curr):
            if not curr:
                return 0
            left_moves = dfs(curr.left)
            right_moves = dfs(curr.right)
            self.moves += abs(left_moves) + abs(right_moves)

            return (curr.val-1)+ left_moves + right_moves
        
        dfs(root)
        return self.moves
