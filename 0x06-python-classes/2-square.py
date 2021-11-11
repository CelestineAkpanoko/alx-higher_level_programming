#!/usr/bin/python3
"""A script that works with squares.
"""


class Square:
    """A class square.
    """
    def __init__(self, size=0):
        """Initializes a square with a given size.
        Args:
            size (int): The size of the square.
        """
        super().__init__()
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
