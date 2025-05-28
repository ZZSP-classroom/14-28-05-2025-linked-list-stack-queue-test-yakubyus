import unittest
from browser_history import Stack


class TestBrowserHistory(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push("http://example.com")
        self.assertEqual(stack.peek(), "http://example.com")

    def test_pop(self):
        stack = Stack()
        stack.push("http://example.com")
        stack.push("http://example2.com")
        popped_page = stack.pop()
        self.assertEqual(popped_page, "http://example2.com")
        self.assertEqual(stack.peek(), "http://example.com")

    def test_peek(self):
        stack = Stack()
        stack.push("http://example.com")
        self.assertEqual(stack.peek(), "http://example.com")


if __name__ == '__main__':
    unittest.main()
