# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # base case
        # if there is no node, 1 node, or 2 nodes
        # don't have to do anything
        if not head or not head.next or not head.next.next: 
            return 
        
        # set up pointers to find middle 
        slow = head
        fast = head 

        while fast and fast.next: # stop looking when fast reaches the end
            slow = slow.next 
            fast = fast.next.next 
        # once fast exists, slow is sitting at the end of the first half 

        # reverse second half 
        curr = slow.next # curr = first node of second half 
        slow.next = None # cut the list inst 2 seperate halves 
        prev = None  # prev = the reversed chain so far (empty at start)

        while curr: # walk through every node of second half 
            temp = curr.next # save the next node 
            curr.next = prev # flip: point curr backwards
            prev = curr  # move prev forward onto curr
            curr = temp # move curr forward onto the saved node 
        
        # now prev is the head of the reversed second half 

        back = prev # back is head of reversed second half 
        front = head # front is head of first half 

        while back: # stop when the back half runs out 
            front_temp = front.next # save front's next 
            back_temp = back.next # save back's next 
            front.next = back # link front --> back
            back.next = front_temp # link back --> front's old next
            front = front_temp # advance front
            back = back_temp  # advance back 
        
        return  
            
