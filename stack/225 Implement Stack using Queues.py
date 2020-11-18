class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        self.s_len=-1

        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        self.s_len+=1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.s_len-=1
        return(self.stack.pop())
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return(self.stack[self.s_len])
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return(self.s_len<0)
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.empty()
print(obj.top())
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()