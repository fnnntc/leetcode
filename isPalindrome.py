class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return True
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        return vals==vals[::-1]
            