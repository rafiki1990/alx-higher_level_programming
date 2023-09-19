#!/usr/bin/python3
"""Define test_square.

This module defines the tests run on the Square class.
"""

import unittest
from models.square import Square
from tests.test_models.test_rectangle import TestRectangle


class TestSquare(TestRectangle):
    """Test case class for testing the Square class."""

    # Since TestSquare inherits from TestRectangle,
    # it will automatically include all the test cases from TestRectangle.

    def test_square_specific_method(self):
        """Test specific methods or properties of the Square class."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_area(self):
        """Test the area method for the Square class."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s = Square(8)
        self.assertEqual(s.area(), 64)

    def test_square_str_representation(self):
        """Test the string representation (__str__) of the Square class."""
        s = Square(4, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 4")

    def test_square_update_method(self):
        """Test the update method for the Square class."""
        s = Square(3, 1, 2, 1)

        # Update with positional arguments
        s.update(5, 6, 7, 8)  # This updates id=5, size=6, x=7, y=8
        self.assertEqual(s.__str__(), "[Square] (5) 7/8 - 6")

        # Update with keyword arguments
        s.update(id=10, size=4)
        self.assertEqual(s.__str__(), "[Square] (10) 7/8 - 4")

    def test_square_to_dictionary_method(self):
        """Test the to_dictionary method for the Square class."""
        s = Square(5, 2, 3, 1)
        my_dict = s.to_dictionary()
        expected_dict = {'id': 1, 'x': 2, 'size': 5, 'y': 3}
        self.assertDictEqual(my_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
