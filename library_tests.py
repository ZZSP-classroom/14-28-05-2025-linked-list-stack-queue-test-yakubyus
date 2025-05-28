import unittest
from library_reservation import Queue, Reservation


class TestLibraryReservationSystem(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        reservation = Reservation("Alicja", "sadasd")
        queue.enqueue(reservation)
        self.assertEqual(queue.peek().user_name, "Alicja")
        self.assertEqual(queue.peek().book_title, "sadasd")

    def test_dequeue(self):
        queue = Queue()
        reservation1 = Reservation("Alicja", "sadasd")
        reservation2 = Reservation("Jan", "xxx")
        queue.enqueue(reservation1)
        queue.enqueue(reservation2)
        dequeued_reservation = queue.dequeue()
        self.assertEqual(dequeued_reservation.user_name, "Alicja")
        self.assertEqual(dequeued_reservation.book_title, "sadasd")
        self.assertEqual(queue.peek().user_name, "Jan")

    def test_peek(self):
        queue = Queue()
        reservation1 = Reservation("Alicja", "sadasd")
        queue.enqueue(reservation1)
        self.assertEqual(queue.peek().user_name, "Alicja")
        self.assertEqual(queue.peek().book_title, "sadasd")


if __name__ == '__main__':
    unittest.main()
