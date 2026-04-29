class MyQueue:

    def __init__(self):
        self.stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack_size = len(self.stack)
        for i in range(stack_size - 1):
            top_ele = self.stack.pop()
            self.helper_stack.append(top_ele)
        
        front_ele = self.stack.pop()

        for i in range(stack_size - 1):
            top_ele = self.helper_stack.pop()
            self.stack.append(top_ele)

        return front_ele
        

    def peek(self) -> int:
        return self.stack[0]        

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()