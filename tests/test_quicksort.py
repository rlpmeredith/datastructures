import unittest

from quicksort import swap_items


class TestQuicksort(unittest.TestCase):

    def test_swap_items(self):
        
        # Arrange
        my_list = [1,2,3,4]

        # Act
        sorted1 = swap_items(0,2)

        # Assert
        self.assertEqual([3,2,1,4], sorted1, "Swap items not right")
































