#!/usr/bin/python3
"""
Module 4-square
Defines a square based on 3-square.py
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
        self.size = size

    @property
    def size(self):
        """
        Getter for size.
        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

