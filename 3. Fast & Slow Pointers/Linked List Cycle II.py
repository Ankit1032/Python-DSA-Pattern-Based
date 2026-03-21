# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First intuition was too solve it by using hashmap where i store the node with their position as value and keep checking

        #We will solve in 2 steps
        #1. First we will detect the cycle
        #2. assign slow to head and we will iterate slow and fast with one jump
        #3. the node they meet will be the node with is linked
        #Floyd cycle detection proves it

        slow = head
        fast = head
        
        #Detect Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Cycle is detected
            if slow == fast:
                #Assign slow to head
                slow = head
                
                # Make slow and fast jump one at a time
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        #If no cycle detected
        return None
        
