#!/usr/bin/python3
"""
Module 1-square
Defines a square based on 0-square.py
"""


class Square:
    """
    This is a class for a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """
        Initializes the square.
        Args:
            size (int): size of the square.
        """
        self.__size = size
