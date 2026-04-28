# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float("-inf")

        def dfs(root):
            if not root:
                return 0

            left_child = max(dfs(root.left),0)
            right_child = max(dfs(root.right),0)

            curr = root.val + left_child + right_child
            self.max_sum = max(self.max_sum,curr)

            return root.val + max(left_child, right_child)
        dfs(root)
        return self.max_sum

