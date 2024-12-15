from pysvt import test

data = {
    "i": ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin",
          [], [-2], [0], [-3], [], [], [], []],
    "o": [[None, None, None, None, -3, None, 0, -2]],
}

@test(data=data, method="minStack")
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) 

    def pop(self) -> None:
        if self.stack:
            element = self.stack.pop()

            if element == self.min_stack[-1]:
                self.min_stack.pop()
        else:
            return "stack is empty"

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return "stack is empty"

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return "empty stack"

