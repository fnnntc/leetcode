# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None:
            return False
        try:
            cur=head
            if cur.next:
                nxt=cur.next
            else:
                return False
            while not cur==nxt:
                print(cur,nxt)
                cur=cur.next
                nxt=nxt.next.next
            return True

        except:
            return False