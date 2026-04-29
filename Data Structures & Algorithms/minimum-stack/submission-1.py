class MinStack:

    def __init__(self):
        self.stack = []
        self.track = []

    def push(self, val: int) -> None:
        if self.track and val < self.track[-1]:
            self.track.append(val)
        elif self.track:
            self.track.append(self.track[-1])
        else:
            self.track.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.track.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.track[-1]
