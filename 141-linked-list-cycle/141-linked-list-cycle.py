# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        a = head
        b = head.next
        
        while a != b and b:
            a = a.next
            b = b.next
            
            if not b:
                return False
            
            b = b.next
    
            if not b:
                return False
        
        return True