class Square:
    """Defines a square by size, and has methods to calculate area and print"""

    def __init__(self, size=0):
        """Initialize Square instance with optional size"""
        self.size = size

    @property
    def size(self):
        """Retrieve size of Square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square instance with error checking"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of Square instance"""
        return self.__size * self.__size

    def my_print(self):
        """Print Square instance using '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

