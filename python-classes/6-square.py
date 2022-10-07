#!/usr/bin/python3
"""Square class with attributes"""


class Square:

    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new Square"""
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__ (self, position=(0, 0)):
        """Initialize the position"""
        self.__position = position

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
            return
        else: 
            for i in range(0, self.__position):
                print()
            for j in range(0, self.__size):
                for h in range(0, self.__position):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print()
