"""Creating a point Class that scales its cordinates."""


from __future__ import annotations


class Point:
    """Class Point."""
    x: float
    y: float

    def __init__(self, x_int: float, y_int: float):
        """My contructor."""
        self.x = x_int
        self.y = y_int
    
    def scale_by(self, factor: int) -> None: 
        """Scale the point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point: 
        """Scale the point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point