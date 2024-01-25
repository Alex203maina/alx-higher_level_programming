class Square:
    """Defines a square by size, and has methods to calculate area and compare squares"""

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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of Square instance"""
        return self.__size * self.__size

    def __lt__(self, other):
        """Compare if this square is less than another based on area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if this square is less than or equal to another based on area"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Compare if this square is equal to another based on area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if this square is not equal to another based on area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if this square is greater than another based on area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if this square is greater than or equal to another based on area"""
        return self.area() >= other.area()

