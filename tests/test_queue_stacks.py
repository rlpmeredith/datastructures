import unittest

from queue_stacks import QueueStack

class TestQueueStack(unittest.TestCase):

    def test_enqueue_dequeue(self):
        
        # Arrange
        my_queue = QueueStack()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        
        # Act
        dequeue1 = my_queue.dequeue()
        dequeue2 = my_queue.dequeue()
        
        # Assert
        self.assertEqual(1, dequeue1, "first dequeue did not have the expected value")
        self.assertEqual(2, dequeue2, "second dequeue did not have the expected value")

    def test_enqueue_dequeue_enqueue(self):
        # Arrange
        my_queue = QueueStack()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.dequeue()

        # Act
        my_queue.enqueue(3)
        my_queue.enqueue(4)
        dequeue1 = my_queue.dequeue()

        # Assert
        self.assertEqual(2, dequeue1, "first dequeue did not have the expected value")

