# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        next = None
        
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
        
        curr = head
        prev = None
        nxt = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            print(curr, prev, nxt)