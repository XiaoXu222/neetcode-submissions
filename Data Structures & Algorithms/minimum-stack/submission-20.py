class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minValue = 0       

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minValue = val
        else:
            self.minValue = min(self.minValue, val)
        self.minStack.append(self.minValue)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if not self.minStack:
            self.minValue = 0
        else:
            self.minValue = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minValue
        
