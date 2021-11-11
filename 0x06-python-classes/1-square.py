#!/usr/bin/python3
"""A file describing a class with init function (construction).
"""


class Square:
    """A class square with an init function.
    """
    def __init__(self, size):
        """Initializes a Square with a given size.
        Args:
            size (int): The size of the square.
        """
        super().__init__()
        self.__size = size
