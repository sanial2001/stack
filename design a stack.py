class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.n = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) > k:
            i = 0
            while i < k:
                self.stack[i] += val
                i += 1
        else:
            for i in range(len(self.stack)):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
