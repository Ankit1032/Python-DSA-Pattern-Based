# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #Step1: Get the slow pointer in the middle of the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #step2 : Reverse the list from slow/middle position till very end
        prev, curr = None, slow.next
        slow.next = None

        # we kept prev as None and Slow.next as None to destroy the connection between the two halves to order the list properly

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #Step 3 : Reordering the list (prev points to end node)
        lp = head
        rp = prev

        while rp:
            ln = lp.next
            rn = rp.next
            lp.next = rp
            rp.next = ln
            lp = ln
            rp = rn
        
        
