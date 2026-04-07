# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def validate(node):
            if not node:
                return True, float('inf'), float('-inf'), 0

            lis_valid, l_min, l_max, l_sum = validate(node.left)
            ris_valid, r_min, r_max, r_sum = validate(node.right) 

            if lis_valid and ris_valid and l_max < node.val <r_min:
                sums = l_sum + node.val + r_sum
                self.max_sum = max(self.max_sum, sums)
                return True, min(l_min, node.val), max(r_max, node.val), sums
            else:
                sums = 0
                return False,0,0,0

        validate(root)
        return self.max_sum