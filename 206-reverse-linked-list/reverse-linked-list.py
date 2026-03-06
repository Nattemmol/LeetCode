# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        
        l,r = 0,len(ans)-1

        while l < r:
            ans[l],ans[r] = ans[r], ans[l]
            l += 1
            r -= 1

        dummy = ListNode(-1)
        curr = dummy

        for v in ans:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next
        