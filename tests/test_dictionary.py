import unittest

from dictionary import CustomDictionary


class TestCustomDictionary(unittest.TestCase):

    def test_set_get(self):

        # Arrange
        my_dict = CustomDictionary(100)
        my_dict.set("Key1", 12345)
        my_dict.set("Key2", 67890)

        # Act
        result1 = my_dict.get("Key1")
        result2 = my_dict.get("Key2")

        # Assert
        self.assertEqual(12345, result1, "First set get did not return correct value")
        self.assertEqual(67890, result2, "Second set get did not return correct value")

    def test_contains(self):

        # Arrange
        my_dict = CustomDictionary(100)
        my_dict.set("Key1", 12345)

        # Act
        result1 = my_dict.contains("Key1")
        result2 = my_dict.contains("Key2")

        # Assert
        self.assertEqual(True, result1, "First contains did not return correct value")
        self.assertEqual(False, result2, "Second contains get did not return correct value")


    def test_get_index(self):
        # Arrange
        my_dict = CustomDictionary(100)

        # Act

        # Assert


