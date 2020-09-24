"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val==0 and l1.next==None:
            return l2
        if l2.val==0 and l2.next==None:
            return l1   
        #calc
        d=l3=ListNode(0)
        xn=0
        while l1 or l2:
            if l1==None:
                l1=ListNode(0)
            elif l2==None:
                l2=ListNode(0)
            x=l1.val+l2.val+xn
            xn=0
            if x>9:
                xn=1
                x=x%10
            l3.next=ListNode(x)
            l1,l2,l3=l1.next,l2.next,l3.next
        if xn==1:
            l3.next=ListNode(xn)
        return d.next