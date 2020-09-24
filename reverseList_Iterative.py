# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return
        fast=head
        while fast.next:
            fast=fast.next
        while head!=fast:
            moved=head
            head=head.next
            if fast.next:
                tmp=fast.next
                fast.next=moved
                moved.next=tmp
            else:
                fast.next=moved
                fast.next.next=None
        return head