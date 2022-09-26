#!/usr/bin/python3
"""Square class with attributes"""


class Square:
    """Size private attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raiseTypeError("size must be an integer")
        elif size < 0:
            raiseValueError("size must be >=0")
        self.__size = size
