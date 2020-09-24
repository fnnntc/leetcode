"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head==None:
            return
        cur=head
        while cur.next:
            if cur.child:
                ziel=cur.next
                cur.next=cur.child
                cur.next.prev=cur   # ????
                ret=cur.child
                cur.child=None
                while cur.next:
                    cur=cur.next
                cur.next=ziel
                ziel.prev=cur    # ???
                cur=ret
            else:
                cur=cur.next
        return head