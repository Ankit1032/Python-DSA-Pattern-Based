# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        if head.next.next is None:
            return head.next

        slow = head
        fast = head

        while fast is not None and fast.next is not None: #as 'fast' jumps faster/longer than 'slow', we only tend to check if fast and fast.next is None or not
            slow = slow.next
            fast = fast.next.next

        return slow
