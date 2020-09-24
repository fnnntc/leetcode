    def oddEvenList(self, head):
        #1 2 3 4 5
        if head==None:
            return
        if head.next==None:
            return head
        odd=head
        even=head.next
        eHead=even
        while even and even.next:
            print(odd.val)
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next.next=eHead
        