#!/usr/bin/python3
"""Define a Rectangle class"""

class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initiitalize a mew rectangle.

        Args:
        width (int): the width of the recrangle.
        height (int): the height of the new rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <0:
                raise ValueError("widht must be >=9")
            self.__width = value

            @property
            def height(self):
                """get the height of the rectangle"""
                return self.__height

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >=0")
                self.__height = value
