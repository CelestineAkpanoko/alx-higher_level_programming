#!/usr/bin/python3
"""A script that works with squares.
"""


class Square:
    '''A class square.
    '''
    def __init__(self, size=0):
        '''Initializes a Square with a given size.
        Args:
            size (int): The size of the square.
        '''
        self.size = size

    @property
    def size(self):
        '''Retrieves the size of this Square.
        Returns:
            int: The size of this Square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Updates the size of this Square.
        Args:
            value (int): The new size of this Square.
        '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        '''Computes the area of this Square.
        Returns:
            int: The area of this Square.
        '''
        return self.size ** 2

    def my_print(self):
        '''Prints a square with '#'.
        '''
        if self.size == 0:
            print('')
        else:
            for i in range(self.size):
                print('{}'.format('#' * self.size))
