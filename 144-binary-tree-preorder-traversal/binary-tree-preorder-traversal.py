# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preOrder(self, root, res):
            if not root:
                return
            res.append(root.val)
            self.preOrder(root.left, res)
            self.preOrder(root.right, res)
    def preorderTraversal(self, root):
        res = []
        self.preOrder(root, res)
        return res
       

        