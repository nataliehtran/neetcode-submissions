# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # given: head
        
        # tortise and hare 

        slow = head
        fast = head

        while fast and fast.next: # make sure fast.next is not null because shifting fast by 2 at each iteration 
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast: 
                return True 


        return False # no cycle 

        # if cycle, return true 
        # no cycle, return false 