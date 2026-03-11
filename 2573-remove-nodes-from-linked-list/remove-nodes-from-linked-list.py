# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = deque()

        curr = head

        while curr:
            while ans and curr.val > ans[-1]:
                ans.pop()
            ans.append(curr.val)
            curr = curr.next

        
        if not ans:
            return None
        head2 = ListNode(ans[0])
        ans.popleft()
        current = head2
        for element in ans:
            current.next = ListNode(element)
            current = current.next
        return head2
            