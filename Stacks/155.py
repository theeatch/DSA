from pysvt import test

data = {
    "i": ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin",
          [], [-2], [0], [-3], [], [], [], []],
    "o": [[None, None, None, None, -3, None, 0, -2]],
}

@test(data=data, method="minStack")
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or the current value is smaller than the top of min_stack, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If the value popped is the same as the top of min_stack, pop it from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Ensure the number of input operations and expected outputs match
assert len(data["i"][0]) == len(data["o"]), "Input and output data lengths do not match"

# The test decorator will handle running the tests based on the provided data
