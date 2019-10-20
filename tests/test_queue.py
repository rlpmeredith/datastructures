import unittest

from queue import Queue

class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        
        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        
        # Act
        dequeue1 = my_queue.dequeue()
        dequeue2 = my_queue.dequeue()
        
        # Assert
        self.assertEqual(1, dequeue1, "first dequeue did not have the expected value")
        self.assertEqual(2, dequeue2, "second dequeue did not have the expected value")

    def test_peek(self):

        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)

        # Act
        peek1 = my_queue.peek()

        # Assert
        self.assertEqual(1, peek1, "peek did not have the expected value")

    def test_length(self):

        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)

        # Act
        length1 = my_queue.__len__()

        # Assert
        self.assertEqual(2, length1, "length did not have the expected value")

