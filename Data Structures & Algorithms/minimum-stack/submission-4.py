class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.miniStack) == 0:
            self.miniStack.append(val)
        else:
            self.miniStack.append(min(self.miniStack[-1], val))
        # print('push: ', self.miniStack)

    def pop(self) -> None:
        self.miniStack.pop()
        # print('pop: ',self.miniStack)
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miniStack[-1]
        
