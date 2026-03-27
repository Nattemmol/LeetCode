# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sums = 0
    trav = []
    trav_sum = [0]
    

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = 0
        if not root:
            return 0
        
        self.trav.append(root.val)
        
        add = self.trav_sum[-1] + self.trav[-1]

        count += self.trav_sum.count(add - targetSum)

        self.trav_sum.append(add)

        if not root.left and not root.right:
            self.trav.pop()      
            self.trav_sum.pop()
            return count
        
        if root.left:
            count += self.pathSum(root.left, targetSum)

        if root.right:
            count += self.pathSum(root.right, targetSum)
        
        self.trav.pop()
        self.trav_sum.pop()

        return count
