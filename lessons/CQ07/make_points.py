"""Test the point class."""
from lessons.CQ07.point import Point

cordinate: Point = Point(5, 3)

print(cordinate.scale_by(5))
print(cordinate.scale_by(3))