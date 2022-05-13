# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if (head == None): #IF there is no head than we dont got a cycle
            return False
        elif (head.next == None): #If there is no next head, there isn't a cycle
            return False
        
        h1=h2=head
        while (h2 and h2.next):   #We check if h2 and the next head exist to confirm cycle of 2+ size
            h1,h2 = h1.next,h2.next.next    #We keep looping to see if h1 and h2 equal each other as we go to the next heads
            if (h1 == h2):
                return True    #Eventually, they should equal the same value
        return False   #If there isnt a h2 or a new h2 value after, we break
            