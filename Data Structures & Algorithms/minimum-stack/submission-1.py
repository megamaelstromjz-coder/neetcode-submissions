class MinStack:

    def __init__(self):
        self.x = []
        self.mini = []
        

    def push(self, val: int) -> None:
        self.x.append(val)
        if not self.mini or self.mini[-1] >= val:
            self.mini.append(val)
        

    def pop(self) -> None:
        x = self.x.pop()
        if self.mini and self.mini[-1] == x:
            self.mini.pop()

    def top(self) -> int:
        return self.x[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]

        
