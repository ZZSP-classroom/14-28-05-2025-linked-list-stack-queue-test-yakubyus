import unittest
from support_ticket import Queue, Stack, Ticket


class TestSupportTicketSystem(unittest.TestCase):
    def test_ticket_queue(self):
        queue = Queue()
        ticket1 = Ticket(1, "Login issue")
        ticket2 = Ticket(2, "Page not loading")
        queue.enqueue(ticket1)
        queue.enqueue(ticket2)
        self.assertEqual(queue.peek().ticket_id, 1)
        dequeued_ticket = queue.dequeue()
        self.assertEqual(dequeued_ticket.ticket_id, 1)
        self.assertEqual(queue.peek().ticket_id, 2)

    def test_ticket_stack(self):
        stack = Stack()
        ticket1 = Ticket(1, "Login issue")
        ticket2 = Ticket(2, "Page not loading")
        stack.push(ticket1)
        stack.push(ticket2)
        self.assertEqual(stack.peek().ticket_id, 2)
        popped_ticket = stack.pop()
        self.assertEqual(popped_ticket.ticket_id, 2)
        self.assertEqual(stack.peek().ticket_id, 1)


if __name__ == '__main__':
    unittest.main()
