#Imports
import re
import numpy as np

class Vector2D:
    def __init__(self, coordinates, color="black", _components = []):
        self.coordinates = np.array(coordinates, dtype=np.float64)
        if self.coordinates.shape != (2,):
            raise Exception("Vector2D coordinates must be of length 2")
        self.color=color
        self._components = _components.copy()
        if len(self._components) == 0:
            self._components.append(self)
        
    def __str__(self) -> str:
        return self.coordinates.__str__()
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        if type(other) == np.ndarray and other.shape == (2,):
            return self.coordinates + other
        elif type(other) == Vector2D:
            _components = []
            _components.extend(self._components)
            _components.extend(other._components)
            return Vector2D(self.coordinates + other.coordinates, _components=_components)
        else:
            raise Exception("Vector2D must be added either to other Vector2D or ndarray of shape 2.")
    
    def __getitem__(self, item):
        return self.coordinates[item]