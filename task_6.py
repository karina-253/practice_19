import math


class Point:
    """
    A class representing a point on a plane.

    This class allows you to create points with (x, y) coordinates, calculate
    the distance between the points, sum the coordinates of the points and get
    a string representation of a point.

    Attributes:
        x (float or int): X-coordinate of the point.
        y (float or int): Y-coordinate of the point.
    """

    def __init__(self, axis: tuple = (0,0)) -> None:
        """
        Initializes a new Point object.
        Args:
            axis (tuple): A tuple of two numbers (x, y). The default value is (0, 0).
        """
        self.x = axis[0]
        self.y = axis[1]

    def get_x(self) -> float:
        """
        Returns the X coordinate of the point.

        Returns:
            float or int: X coordinate.
        """
        return self.x

    def get_y(self) -> float:
        """
        Returns the Y coordinate of the point.

        Returns:
            float or int: Y coordinate.
        """
        return self.y

    def distance(self, other) -> float:
        """
        Calculates the distance between the current point and another point
        using the Euclidean distance formula.
        Args:
            other: The other point to which the distance is calculated.

        Returns:
            float: The distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def sum(self, other):
        """
        Creates a new point with coordinates equal to the sum of the coordinates of two points.

        Args:
            other: Another point whose coordinates are added to the current point.

        Returns:
            Point: A new Point object with coordinates
        """
        return Point((self.x + other.x, self.y + other.y))

    def __str__(self) -> str:
        """
        Returns a string representation of a point

        Returns:
            str: A string like (x, y)
        """
        return f"({self.x}; {self.y})"

    def __repr__(self) -> str:
        """
        Returns a point representation for debugging.

        Returns:
            str: A string that allows you to recreate the Point object.
        """
        return f"Point({(self.x, self.y)})"

p = Point((3,-7))
print(p)
a = Point()
print(a)
print(a.get_x())
print(p.get_y())
c = Point((-2, 4))
print(p.distance(c))
d = c.sum(p)
print(d)
