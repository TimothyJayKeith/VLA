#Import packages
import numpy as np

class Circle:
    def __init__(self, radius=1.0, color="black") -> None:
        self.radius = radius
        self.color = color

class PGraph2D:
    def __init__(self, f1, f2, color="black") -> None:
        self.f1 = f1
        self.f2 = f2
        self.color = color

class FGraph2D(PGraph2D):
    def __init__(self, f, color="black") -> None:
        self.f1 = lambda t: t
        self.f2 = f
        self.color = color
    
    def __getitem__(self, item):
        self.f2(item)

class Polygon:
    def __init__(self, vertices, color="black") -> None:
        self.vertices = np.array(vertices)
        self.color = color

class Text:
    def __init__(self, text) -> None:
        self.text = text