#!/usr/bin/python3
"""Define Square module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square class, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Define getter for the private attribute size."""
        return self.width

    @size.setter
    def size(self, value):
        """Define setter for private attribute size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Define the string representation of the Square."""
        return ("[Square] ({}) {}/"
                "{} - {}".format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance.

        Args:
                *args:      A tuple containing the values for id, size, x,
                            and y in the specified order.

                **kwargs:   Key-value pairs representing attributes
                            to be updated.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Define to_dictionary method.

        It returns the dictionary representation of the Square.
        """
        my_dict = {
                    'id': self.id,
                    'x': self.x,
                    'size': self.size,
                    'y': self.y

                    }

        return my_dict
