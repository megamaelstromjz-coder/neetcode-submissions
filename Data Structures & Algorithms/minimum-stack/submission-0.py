class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minVals:
            self.minVals.append(value)
        else:
            self.minVals.append(min(value, self.minVals[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minVals.pop()
        
    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minVals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()