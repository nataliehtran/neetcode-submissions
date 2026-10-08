# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head 
        while curr: 
            # stash the rest of hte list before we lose 
            nxt = curr.next 
            # flip node pointer backwards
            curr.next = prev 
            # advance prev 
            prev = curr
            # advance curr
            curr = nxt 
        # prev is new head
        return prev 