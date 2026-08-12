class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []
        self.mini = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini = val
        else:
            self.mini = min(self.mini, val)

        self.stack.append(val)
        self.miniStack.append(self.mini)
        
    def pop(self) -> None:
        self.stack.pop()
        self.miniStack.pop()
        if self.stack:
            self.mini = self.miniStack[-1]
        else:
            self.mini = 0
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini
        
