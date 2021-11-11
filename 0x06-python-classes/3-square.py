#!/usr/bin/python3
"""A script that works with squares.
"""


class Square:
    """A class square.
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.
        Args:
            size (int): The size of the square.
        """
        super().__init__()
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """Computes the area of this Square.
        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
