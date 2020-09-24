class MySinglyNode:
    
    def __init__(self, val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index==0:
            return self.head

        else:
            cur=self.head
            for i in range(index):
                if cur.next:
                    cur=cur.next
                else:
                    return -1
            return cur.val
            
            
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node=MySinglyNode(val)
        if node.next:
            node.next=self.head
        self.head=node        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur=self.head
        while cur.next:
            cur=cur.next
        node=MySinglyNode(val)
        cur.next=node
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur=self.head
        node=MySinglyNode(val)
        if index==0:
            self.addAtHead(val)
            return
        for i in range(index-1):
            print("i",cur.val)
            if cur.next:
                cur=cur.next
            else:
                return
        node.next=cur.next
        cur.next=node
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index==0:
            self.head=self.head.next
            return
        cur=self.head
        for i in range(index-1):
            print("i",cur.val)
            if cur.next:
                cur=cur.next
            else:
                return
        if cur.next:
            cur.next=cur.next.next
        else:
            cur.next=None

    def printList(self):
        cur=obj.head
        while cur:
            print(cur.val)
            cur=cur.next
        print("end")

    def isPalindrome(self,head):
        if head==None or head.next==None:
            return True
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        return vals==vals[::-1]
            
        

# Your MyLinkedList object will be instantiated and called as such:
#["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
#[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
obj = MyLinkedList()
obj.printList()
#param_1 = obj.get(1)
"""obj.addAtHead(2)
obj.printList()
obj.deleteAtIndex(1)
obj.printList()
obj.addAtHead(2)
obj.printList()
obj.addAtHead(7)
obj.printList()
obj.addAtHead(3)
obj.printList()
obj.addAtHead(2)
obj.printList()
obj.addAtHead(5)
obj.printList()
obj.get(0)
"""


obj.addAtHead(1)
obj.addAtTail(2)
#obj.addAtTail(2)
#obj.addAtTail(1)
obj.printList()

obj.isPalindrome(obj.head)
