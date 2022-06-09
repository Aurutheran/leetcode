# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original = []
        
        if not head:
            return head
        
        point = head
        while (point.next != None):
            
            if (point.val == point.next.val):
                point.next = point.next.next
            else:
                point = point.next
                
        return head
        
        