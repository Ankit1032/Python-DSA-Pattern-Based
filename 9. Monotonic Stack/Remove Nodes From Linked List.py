# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Monotonic Stack Intuition - Same as next greater element
        stack = []

        curr = head
        while curr:
            curr_ele = curr.val

            while stack and curr_ele > stack[-1]:
                stack.pop()
            stack.append(curr_ele)
            curr = curr.next

        new_head = ListNode(0)
        curr = new_head
        for i in stack:
            curr.next = ListNode(i)
            curr = curr.next

        return new_head.next
