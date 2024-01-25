#!/usr/bin/python3
"""
Module 3-square
Defines a square based on 2-square.py
"""


class Square:
    """
    This is a class for a square.
    Private instance attribute: size.
    Instantiation with optional size: def __init__(self, size=0).
    """

    def __init__(self, size=0):
        """
        Initializes the square.
        Args:
            size (int, optional): size of the square, defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

