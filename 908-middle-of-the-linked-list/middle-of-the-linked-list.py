# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        
        left = head
        right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        

        return left