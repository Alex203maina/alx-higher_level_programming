class Square:
    """Defines a square by size and position, and has methods to calculate area and print"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square instance with optional size and position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve position of Square instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of Square instance with error checking"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area of Square instance"""
        return self.__size * self.__size

    def my_print(self):
        """Print Square instance using '#' character, considering position"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

