class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.arr = [0] * self.capacity
            self.length = 0

    def get(self, i: int):
        element = self.arr[i]
        return element

    def set(self, i: int, n: int):
        self.arr[i] = n

    def pushback(self, n: int):
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self):
        element = self.arr[self.length-1]
        self.arr[self.length-1] = 0
        self.length -= 1
        return element
 
    def resize(self):
        self.capacity *= 2
        newArr = [0] * self.capacity
        for i in range (self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def getSize(self):
        return self.length
  
    def getCapacity(self):
        return self.capacity
