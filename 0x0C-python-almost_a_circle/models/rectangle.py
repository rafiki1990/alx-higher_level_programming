#!/usr/bin/python3
"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Define Rectangle class.

    Private instance attributes, each with its own public getter and setter:
    - __width -> width
    - __height -> height
    - __x -> x
    - __y -> y

    Class constructor:
    def __init__(self, width, height, x=0, y=0, id=None):
        Call the super class with id - this super call with use the
        logic of the __init__ of the Base class
        Assign each argument width, height, x, and y to the right attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance."""
        super().__init__(id)  # Call the _init_ method of Base class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Define getter for the private attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Define getter for private attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Define the getter for private attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Define the setter for private attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Define getter for private attribute x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Define setter for private attribute x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Define getter for private attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Define the setter for private attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Define area method."""
        return self.__width * self.__height

    def display(self):
        """Define display method."""
        for _ in range(self.y):
            print()  # Print empty lines for the y offset

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Define the string representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/"
                "{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle instance.

        Args:
                *args:      A tuple containing the values for id, width,
                            height, x, and y in the specified order.

                **kwargs:   Key-value pairs representing attributes to be
                            updated.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Define to_dictionary method.

        It returns the dictionary representation of the Rectange.
        """
        my_dict = {
                    'x': self.x,
                    'y': self.y,
                    'id': self.id,
                    'height': self.height,
                    'width': self.width

                    }

        return my_dict
