class Stack:
    def __init__(self):
        self.stack = []

    def push(self, webpage):
        self.stack.append(webpage)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
