# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # As we need to do it in O(1) space, we cannot use array for comparison

        #Step 1: reach to the middle of the list. The slow pointer will be in middle when the fast pointer reaches to the end
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Step 2: Reverse the linked list from the middle till the end
        prev, curr = slow, slow.next
        slow.next = None #if we dont do this, we reverse/create bidirectional links which will cause problems

        while curr: #once curr becomes none, loop breaks, so prev will be pointing to last node
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: Compare the list from front and back
        left = head
        right = prev

        while left and right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next

        if right:
            return False
        
        return True


        
