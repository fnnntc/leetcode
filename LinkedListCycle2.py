# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return None
        try:
            slow=fast=head
            while slow and fast:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    break
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next    
            return slow
        except:
            return None