# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        ans = 0


        while queue:
            for i in range(len(queue)):
                grandpa = queue.popleft()
                if grandpa.left:
                    queue.append(grandpa.left)
                    if grandpa.val % 2 == 0:
                        if queue[-1].left:
                            ans += queue[-1].left.val
                        if queue[-1].right:
                            ans += queue[-1].right.val
                if grandpa.right:
                    queue.append(grandpa.right)
                    if grandpa.val % 2 == 0:
                        if queue[-1].left:
                            ans += queue[-1].left.val
                        if queue[-1].right:
                            ans += queue[-1].right.val
            
        return ans