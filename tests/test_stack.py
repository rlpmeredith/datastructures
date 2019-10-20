import unittest

from stack import Stack


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        
        # Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        
        # Act
        pop1 = my_stack.pop()
        pop2 = my_stack.pop()
        
        # Assert
        self.assertEqual(2, pop1, "first pop did not have the expected value")
        self.assertEqual(1, pop2, "second pop did not have the expected value")

    def test_peek(self):

        # Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)

        #Act
        peek1 = my_stack.peek()

        #Assert
        self.assertEqual(2, peek1, "peek did not have the expected value")

    def test_length(self):

        # Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)

        # Act
        len1 = my_stack.__len__()

        # Assert
        self.assertEqual(2, len1, "length did not have the expected value")

    def test_empty_stack(self):

        my_stack = Stack()

        self.assertRaises(Exception, my_stack.pop)
