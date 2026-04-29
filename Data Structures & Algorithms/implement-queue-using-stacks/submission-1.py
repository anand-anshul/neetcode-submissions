class MyQueue:

    def __init__(self):
        self.main = []
        self.hell = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        n = len(self.main)
        for i in range(n):
            back = self.main.pop()
            self.hell.append(back)
        res = self.hell.pop()
        m = len(self.hell)
        for i in range(m):
            front = self.hell.pop()
            self.main.append(front)
        return res

    def peek(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()