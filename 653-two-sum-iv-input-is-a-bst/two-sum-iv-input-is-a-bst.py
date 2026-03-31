# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return None
        pos = []
        def traverse(root,pos):     
            if not root:
                return None

            traverse(root.left, pos)
            pos.append(root.val)
            traverse(root.right, pos)
        traverse(root,pos)

        

        left, right = 0, len(pos) - 1
        while left < right:
            current_sum = pos[left] + pos[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return False