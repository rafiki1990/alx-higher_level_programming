#!/usr/bin/python3
import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from tests.test_models.test_base import TestBase


class TestRectangle(unittest.TestCase):
    """Test case class for testing the Rectangle class."""

    def test_attributes_present(self):
        """Test when all arguments are present."""
        b = Rectangle(4, 5, 10, 20, 1)
        self.assertIsNotNone(b.width)
        self.assertIsNotNone(b.height)
        self.assertIsNotNone(b.x)
        self.assertIsNotNone(b.y)
        self.assertIsNotNone(b.id)

    def test_attribute_absent(self):
        """Test when no argument provided at all."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        """Test only one argument."""
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_two_arguments(self):
        """Test two arguments."""
        b = Rectangle(4, 5)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, 0)
        self.assertIsNotNone(b.id)

    def test_three_arguments(self):
        """Test case when only 3 arguments are provides.
        By default, the x and y values should be zero.
        Also the value of id should not be empty.
        """
        b = Rectangle(4, 5, 10)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 10)
        self.assertEqual(b.y, 0)
        self.assertIsNotNone(b.id)

    def test_four_arguments(self):
        """Test four arguments."""
        b = Rectangle(4, 5, 6, 7)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 6)
        self.assertEqual(b.y, 7)
        self.assertIsNotNone(b.id)

    def test_excess_arguments(self):
        """Test excess arguments.
        We are testing when the arguments are more than 5.
        We are only allowed to work with 5 arguments according
        to the definition of our class.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_non_int_width(self):
        """Test when a non-integer is parssed as an argument."""
        with self.assertRaises(TypeError):
            Rectangle('2', 2, 4)

        with self.assertRaises(NameError):
            Rectangle(width, 3, 5, 5)

    def test_non_int_height(self):
        """Test when the height value is not an integer."""
        with self.assertRaises(TypeError):
            Rectangle(2, '2', 4)

        with self.assertRaises(NameError):
            Rectangle(2, height, 4)

    def test_float(self):
        """Test float width or height."""
        with self.assertRaises(TypeError):
            Rectangle(2.3, 4, 4)

        with self.assertRaises(TypeError):
            Rectangle(2, 3.5, 5)

    def test_zero_width_and_height(self):
        """Test when either height or width is zero."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 4)

        with self.assertRaises(ValueError):
            Rectangle(2, 0, 4)

        with self.assertRaises(ValueError):
            Rectangle(0, 0, 2, 4)

    def test_negative_width_or_height(self):
        """Test when either width or height is less than zero."""

        with self.assertRaises(ValueError):
            Rectangle(-2, 3, 8)

        with self.assertRaises(ValueError):
            Rectangle(2, -3, 4)

    def test_x_or_y_negative(self):
        """Test when either x or y is negative."""
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -2, 3)

        with self.assertRaises(ValueError):
            Rectangle(2, 3, 4, -3)

    def test_x_or_y_non_integer(self):
        """Test with non-integers."""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, '3')

        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, '55')

    def test_custom_id(self):
        """Test a custom_id."""
        custom_id = 42
        r = Rectangle(5, 7, 7, 5, custom_id)
        self.assertEqual(r.id, custom_id)

    def test_width_getter(self):
        """Test the wedth getter."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r.width)

    def test_width_setter(self):
        """Test the width setter."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 20
        self.assertEqual(20, r.width)

    def test_height_getter(self):
        """Test the height getter."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """Test the height setter."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """Test the x getter."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """Test the x setter."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """Test the y getter."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """Test the y setter."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 20
        self.assertEqual(20, r.y)

    """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Testing the area() method.
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """

    def test_area_single_arg(self):
        """Test area with one argument.

        Note that area() methods takes no argument.
        """
        r = Rectangle(2, 3, 4, 4, 5)
        with self.assertRaises(TypeError):
            r.area(2)

    def test_area_normal(self):
        """Test the area for regular numbers."""
        b = Rectangle(8, 30, 3, 1, 3)
        self.assertEqual(240, b.area())

    def test_area_altered_args(self):
        """Test the area of altered values for height and width."""
        b = Rectangle(8, 30, 2)
        b.width = 2
        b.height = 15
        self.assertEqual(30, b.area())

    def test_area_large(self):
        """Test area with large values of width and height."""
        r = Rectangle(123456789, 987654321, 2, 3, 1)
        expected_area = 123456789 * 987654321
        self.assertEqual(expected_area, r.area())

    """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Tesing the display method.
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    def test_display_single_cell(self):
        r = Rectangle(1, 1)
        expected_output = '#'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_display_without_y_exists(self):
        """Test case to check if display method without 'y' exists"""
        r = Rectangle(1, 1)
        expected_output = '#'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_display_exists(self):
        """Test case to check if display method exists"""
        r = Rectangle(1, 1)
        self.assertTrue(hasattr(r, "display"))

    def test_display_larger_rectangle(self):
        r = Rectangle(4, 3)
        expected_output = '####\n####\n####'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_display_rectangle_with_custom_shape(self):
        r = Rectangle(3, 2)
        expected_output = '###\n###'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_display_1_arg(self):
        b = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            b.display(2)

    """
    =================================================================
    Test the __str__ method with different scenerios.
    =================================================================
    """

    def test_str_with_custom_id(self):
        """Test __str__ method with a custom id."""
        r = Rectangle(4, 5, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 4/5"
        self.assertEqual(str(r), expected_str)

    def test_str_with_zero_width_or_height(self):
        """Test __str__ method with width or height set to zero."""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_str_with_negative_x_and_y(self):
        """Test __str__ method with negative x and y values."""
        with self.assertRaises(ValueError):
            Rectangle(4, 5, -1, 2)

        with self.assertRaises(ValueError):
            Rectangle(4, 5, 1, -2)

    """
    =================================================================
    Tests for the update method. Here we are testing different cases.
    =================================================================
    """

    def test_update_with_valid_arguments(self):
        """Test the update method with valid arguments."""
        r = Rectangle(4, 5, 1, 2, 10)

        # Call the update method with new attribute values
        r.update(1, 8, 6, 3, 4)

        # Check if the attributes are updated correctly
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_partial_arguments(self):
        """Test by updating some of the arguments while keeping others."""
        r = Rectangle(4, 5, 1, 2, 10)

        # Call the update method with fewer arguments
        r.update(3, 9)

        # Check if the corresponding attributes are updated correctly
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 9)
        # Other attributes (height, x, y) should remain unchanged
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_with_extra_arguments(self):
        """Test the update method with excess arguments."""
        r = Rectangle(4, 5, 1, 2, 10)

        # Call the update method with extra arguments beyond the required ones
        r.update(7, 11, 9, 8, 10, 12, 13)

        # Check if the corresponding attributes are updated correctly
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 11)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 10)
        # Extra arguments should be ignored

    def test_update_without_arguments(self):
        """Call the method without any arguments."""
        r = Rectangle(4, 5, 1, 2, 10)

        # Call the update method without any arguments
        r.update()

        # Check if the attributes remain unchanged
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_with_key_value_arguments(self):
        """Test the method with key_value arguments."""
        r = Rectangle(2, 3, 4, 7, 10)

        # Call the update method with key_value values.
        r.update(width=12, height=2, x=1, y=3, id=5)

        # checking if the arguments are updated accordingly.
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 5)

    def test_update_with_id_key_word_argument(self):
        """Test with only id key_word argument."""
        r = Rectangle(1, 2, 3, 4, 5)

        # Call the update method with only id key-value.
        r.update(id=10)

        # Checking if the id is updated while the rest are unchanged.
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_one_argument_with_positional(self):
        """Test updating only the one attribute using positional arguments."""
        r = Rectangle(1, 2, 3, 4, 5)

        # Call the update method with only one positional argument.
        r.update(10)

        # check if the id has been updated since it is the first argument.
        self.assertEqual(r.id, 10)

        # Check if the other attributes remained unchanged.
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    """
    =================================================================
    Test the to_dictionary() method.
    =================================================================
    """
    def test_return_type(self):
        """Test if the return type will be a dictionary."""
        r = Rectangle(1, 2, 3, 4, 5)
        my_dict = r.to_dictionary()
        self.assertIsInstance(my_dict, dict)

    def test_dictionary_contents(self):
        """Test the contents of the dictionary."""
        r = Rectangle(10, 2, 1, 9, 1)
        my_dict = r.to_dictionary()
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(my_dict, expected_dict)

    def test_independence_from_original_object(self):
        """Test if the returned dictionary is independent of the orig obj."""
        r = Rectangle(5, 10, 2, 3, 1)
        old_dict = r.to_dictionary()

        # Modify the original object.
        r.width = 15
        r.height = 20
        # Verify that the previously obtained dictionary remains unchanged
        expected = {'x': 2, 'y': 3, 'id': 1, 'height': 10, 'width': 5}
        self.assertDictEqual(old_dict, expected)


if __name__ == '__main__':
    unittest.main()
