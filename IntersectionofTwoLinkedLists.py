class MySinglyNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
        cur=self.head
        while cur:
            print(cur.val)
            cur=cur.next
        print("end")

class Solution:
    def getIntersectionNodeArr(self, headA: MySinglyNode, headB: MySinglyNode) -> MySinglyNode:
        if headA == None or headB==None:
            return None
        if headA==headB:
            return headA
        c1=headA
        c2=headB
        visited=[]
        while c1:
            visited.append(c1)
            c1=c1.next
        while c2:
            if c2 in visited:
                return c2
            c2=c2.next  

        #print(headA.val, headB.val)
    def getIntersectionNode(self, headA: MySinglyNode, headB: MySinglyNode) -> MySinglyNode:
        l1,l2=0,0
        c1,c2 = headA,headB
        while c1:
            l1+=1
            c1=c1.next
        while c2:
            l2+=1
            c2=c2.next
        c1,c2 = headA,headB
        d=abs(l1-l2)
        i=0
        if l1>l2:
            for i in range(d):
                c1=c1.next      
        else:
            for i in range(d):
                c2=c2.next
        while c1:
            print(c1.val,c2.val)  
            if c1==c2:
                return c1
            c1=c1.next
            c2=c2.next
            
        




A = MyLinkedList()
A.addAtHead(4)
A.addAtTail(1)
A.addAtTail(8)
A.addAtTail(4)
A.addAtTail(5)
B = MyLinkedList()
B.addAtHead(5)
B.addAtTail(6)
B.addAtTail(1)
B.addAtTail(8)
B.addAtTail(4)
B.addAtTail(5)


A.printList()
B.printList()

c=Solution()
c.getIntersectionNode(A.head,B.head)
