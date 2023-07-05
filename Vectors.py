#Imports
import numpy as np

class Vector2D:
    def __init__(self, coordinates, color="black"):
        self.coordinates = np.array(coordinates, dtype=np.float64)
        if self.coordinates.shape != (2,):
            raise Exception("Vector2D coordinates must be of length 2")
        self.color=color
        
    def __str__(self) -> str:
        return self.coordinates.__str__()
    
    def __add__(self, other):
        if type(other) == np.ndarray and other.shape == (2,):
            return self.coordinates + other
        else:
            raise Exception("Vector2D must be added either to other Vector2D or ndarray of shape 2.")
    
    def __getitem__(self, item):
        return self.coordinates[item]


if __name__ == "__main__":
    vector = Vector2D([2, 7])
    print(vector[0])