class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 2**31
        self.oldmini = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.stack) == 1):
            self.mini = self.stack[0]
        else:
            self.oldmini.append(self.mini)
            newMini = min(val, self.mini) 
            self.mini = newMini

    def pop(self) -> None:
        if (self.stack[-1] == self.mini) & (len(self.stack) > 1):
            self.mini = self.oldmini[-1]
            self.oldmini.pop()
        if len(self.stack) == 1:
            self.mini = 2**31
        if (self.stack[-1] > self.mini):
            self.oldmini.pop()
        self.stack.pop()
   
            
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini
        
