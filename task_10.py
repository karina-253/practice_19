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
        return f"({(self.x, self.y)})"


class Segment:
    """
    A class representing a line segment on a plane, defined by two points.

    Attributes:
        point_1 (Point): The 1st point of the line segment.
        point_2 (Point): The 2nd point of the line segment.
        one_intersection (bool):A segment intersects only one coordinate axis.
    """
    def __init__(self, point_1, point_2) -> None:
        """
        Initializes a Segment object.
        """
        self.point_1 = point_1
        self.point_2 = point_2
        self.one_intersection = self.check_intersection()

    def check_intersection(self) -> bool:
        """
        Checks if the segment crosses only one coordinate axis.
        Returns:
            bool: True if the segment crosses exactly one axis, otherwise False.
        """
        inters_with_x = (self.point_1.y * self.point_2.y) < 0
        inters_with_y = (self.point_1.x * self.point_2.x) < 0

        if inters_with_x and not inters_with_y:
            return True
        elif inters_with_y and not inters_with_x:
            return True
        else:
            return False

    def __str__(self) -> str:
        """Returns a string representation of a segment."""
        return f"({self.point_1}, {self.point_2})"

    def __repr__(self) -> str:
        """Returns a representation of the segment for debugging."""
        return f"({self.point_1}, {self.point_2})"


class CoordinateSystem:
    """
    A class representing a coordinate system with segments.
    Attributes:
        segments (list): A list of segments added to the plane.
    """
    def __init__(self) -> None:
        """Initializes a new CoordinateSystem object with an empty list of line segments"""
        self.segments = []

    def add_segment(self, segment: Segment) -> None:
        """
        Adds a segment to the plane.
        Args:
            segment (Segment): The segment to be added.
        """
        self.segments.append(segment)

    def axis_intersection(self) -> int:
        """
        Determines the number of segments that intersect only one coordinate axis.

        Returns:
            int: The number of segments whose one_intersection == True.
        """
        return sum(1 for segment in self.segments if segment.one_intersection)

    def __str__(self) -> str:
        """Returns a string representation of a plane with segments."""
        return str(self.segments)

    def __repr__(self) -> str:
        """Returns a representation of the segment for debugging"""
        return str(self.segments)


p1 = Point((-2, 7))
print(p1)
p2 = Point((3, 4))
s1 = Segment(p1, p2)
print(s1)
print(s1.one_intersection)
xy = CoordinateSystem()
xy.add_segment(s1)
p3 = Point((2, -8))
p4 = Point((4, 16))
s2 = Segment(p3, p4)
xy.add_segment(s2)
xy.add_segment(Segment(p4, p2))
xy.add_segment(Segment(Point((-5, 3)), Point((-13, -6))))
print(xy.segments)
print(xy)
print(xy.axis_intersection())

