#Import packages
from Vectors import Vector2D

class Circle:
    def __init__(self, center=[0, 0], radius=1.0, color="black") -> None:
        self.center = Vector2D(center)
        self.radius = radius
        self.color = color