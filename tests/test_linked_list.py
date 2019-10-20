import unittest

from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_insert_pop(self):
        
        # Arrange
        my_list = LinkedList()
        my_list.insert_front("Test1")
        my_list.insert_front("Test2")

        # Act
        pop1 = my_list.pop_front()
        pop2 = my_list.pop_front()

        # Assert
        self.assertEqual("Test2", pop1, "first pop did not have the expected value")
        self.assertEqual("Test1", pop2, "second pop did not have the expected value")

    def test_delete(self):
        # Arrange
        my_list = LinkedList()
        my_list.insert_front("Test3")
        my_list.insert_front("Test3")
        my_list.insert_front("Test1")
        my_list.insert_front("Test2")
        my_list.insert_front("Test3")
        my_list.insert_front("Test3")

        # Act
        my_list.delete("Test3")
        length1 = my_list.list_len
        pop1 = my_list.pop_front()

        # Assert
        self.assertEqual(2, length1, "delete did not result in correct list length")
        self.assertEqual("Test2", pop1, "second pop did not have the expected value")

    def test_length_func(self):
        # Arrange
        my_list = LinkedList()
        my_list.insert_front("Test3")
        my_list.insert_front("Test3")
        my_list.insert_front("Test1")
        my_list.insert_front("Test2")
        my_list.insert_front("Test3")
        my_list.insert_front("Test3")

        # Act
        length1 = my_list.__len__()

        # Assert
        self.assertEqual(6, length1, "delete did not result in correct list length")

    def test_reverse(self):

        # Arrange
        my_list = LinkedList()
        my_list.insert_front("One")
        my_list.insert_front("Two")
        my_list.insert_front("Three")

        # Act
        my_list.reverse()
        revlist = my_list.to_array()

        # Assert
        self.assertEqual(["One","Two", "Three"], revlist , "reverse did not work")
