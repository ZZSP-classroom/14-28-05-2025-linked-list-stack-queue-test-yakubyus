class Ticket:
    def __init__(self, ticket_id, issue_description):
        self.ticket_id = ticket_id
        self.issue_description = issue_description


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ticket):
        self.queue.append(ticket)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ticket):
        self.stack.append(ticket)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
