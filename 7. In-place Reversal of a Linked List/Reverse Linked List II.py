class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        
        dummy = ListNode(0) #Thinsg are easier and easy to handle edge cases when u use dummy node
        dummy.next = head

        #1) reach node at position 'left'
        leftPrev, curr = dummy, head
        for i in range(left - 1): #we need to iterate left - 1 times for 'curr' to reach 'left' pos
            leftPrev, curr = curr, curr.next
        
        #Leftprev will be the left of the 'left' pos node

        #2) Reverse from left to right
        prev = None
        for i in range(right - left + 1): #We need to iterate right - left + 1 times
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #the left node should be connected to the right.next node
        #the left to left node should have the right node as it's next
        #curr will point to the right node of the 'right' pos node
        #prev is the 'right' pos node
    
        # [(0) --> 1 --> 2 --> 3 --> 4 --> 5]
        # left = 2 and right = 4
        # so after 2 --> 3 --> 4 is reversed
        # you want 1 connected to 4 --> leftPrev.next = prev
        # you want 2 connected to 5  --> leftPrev.next.next = curr
        # you must wonder why leftPrev.next.next will work because we never disconnected it as we started prev from None. So do this operation first and then leftPrev.next = prev
        
        #3) Update pointers
        leftPrev.next.next = curr
        leftPrev.next = prev # we need to do this after the above statement as it breaks the next.next from above

        #dummy.next will be the new head
        return dummy.next
