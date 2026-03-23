# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        #1) Get to know the length of the list
        list_len = 0
        curr = head
        prev = None
        while curr:
            list_len += 1
            prev = curr
            curr = curr.next

        #2) if k is bigger than list_len then k % list_len (It works for cases even when its smaller)
        k = k % list_len

        #3) if k is 0 meaning no rotation requried meaning if k is 5 and list length is 5 then 5%5 is 0 
        if k == 0:
            return head
        print(k,"-",list_len)

        #4) Find the node left of the kth node | Remember prev is pointing to last node
        left_of_k = head

        iteration = list_len - k - 1
        
        for i in range(iteration):
            left_of_k = left_of_k.next

        #5) Rotate
        #[1,2,3,4,5] and k = 2
        new_head = left_of_k.next   #new_head = 4
        left_of_k.next = None   #3 -> None [1,2,3] .. [4,5]
        prev.next = head    #5.next = 1 so [4,5,1,2,3]

        return new_head


