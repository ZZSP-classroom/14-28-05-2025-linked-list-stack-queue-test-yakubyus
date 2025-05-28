class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, reservation):
        self.queue.append(reservation)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None
