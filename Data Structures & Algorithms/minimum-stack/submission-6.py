class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
            return
        
        diff = val - self.min
        self.stack.append(diff)

        if diff < 0:
            self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop
        

    def top(self) -> int:
        if self.stack[-1] <= 0:
            return self.min
        
        else:
            return self.min + self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
