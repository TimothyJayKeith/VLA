#Imports
import numpy as np
import numbers
import Objects

class Vector2D:
    def __init__(self, coordinates, color="black", _components=[], name=""):
        if type(coordinates) == Vector2D:
            self.coordinates == coordinates.coordinates
        else:
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
    
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector2D(self.coordinates * other)
        elif type(other) == Vector2D:
            return np.dot(self.coordinates, other.coordinates)
        else:
            raise Exception("Vector2D can only be multiplied by scalar or other Vector2D")
     
    def norm(self):
        return np.linalg.norm(self.coordinates)
    
    def unit_vector(self):
        return self * (1/self.norm())
    
    def project_onto(self, other):
        return other * ((self * other) / (other * other))
    
    def __getitem__(self, item):
        return self.coordinates[item]

class Matrix2x2:
    def __init__(self, coordinates, inverse=None, qr=None, svd=None, eig=None, describe=True) -> None:
        coordinates = np.array(coordinates)
        if coordinates.shape == (2,2):
            self.coordinates = coordinates
        elif coordinates.shape == (2,):
            self.coordinates = np.array([[coordinates[0], 0], [0, coordinates[1]]])
        else:
            raise Exception("Matrix 2x2 coordinates must be either 2x2 array or 2x1 array.")

        if describe:
            try:
                self.inverse = Matrix2x2(np.linalg.inv(coordinates), inverse=self, describe=False)
            except np.linalg.linalg.LinAlgError:
                self.inverse = None

            q, r = np.linalg.qr(self.coordinates)
            self.qr = Matrix2x2(q, describe=False), Matrix2x2(r, describe=False)

            u, s, vh = np.linalg.svd(self.coordinates)
            self.svd = Matrix2x2(u, describe=False), Matrix2x2(s, describe=False), Matrix2x2(vh, describe=False)

            try:
                self.eig = np.linalg.eig(self.coordinates)
            except np.linalg.linalg.LinAlgError:
                self.eig = None

        else:
            self.inverse = inverse
            self.qr = qr
            self.svd = svd
            self.eig = eig

        if self.eig is not None and not (np.allclose(self.eig[1][:,0], self.eig[1][:,1]) or np.allclose(self.eig[1][:,0], -self.eig[1][:,1])):
            self.diag = Matrix2x2(self.eig[0], describe=False), Matrix2x2(self.eig[1], describe=False)
        else:
            self.diag = None
    
    def __str__(self) -> str:
        if self.coordinates.shape == (2,2):
            return self.coordinates.__str__()
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __add__(self, other):
        if type(other) == Matrix2x2:
            Matrix2x2(self.coordinates + other.coordinates)
        else:
            raise Exception("Matrix2x2 can only add with other Matrix2x2.")
        
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Matrix2x2(self.coordinates * other)
        elif type(other) == Vector2D:
            return Vector2D(np.matmul(self.coordinates, other.coordinates))
        elif type(other) == Matrix2x2:
            return Matrix2x2(np.matmul(self.coordinates, other.coordinates))
        elif isinstance(other, Objects.PGraph2D):
            newf1 = lambda t: self.coordinates[0, 0]*other.f1(t) + self.coordinates[0, 1]*other.f2(t)
            newf2 = lambda t: self.coordinates[1, 0]*other.f1(t) + self.coordinates[1, 1]*other.f2(t)
            return Objects.PGraph2D(newf1, newf2)
        elif type(other) == Objects.Polygon:
            new_vertices = []
            for vertex in other.vertices:
                new_vertices.append(np.matmul(self.coordinates, vertex))
        else: 
            raise Exception("Invalid object for multiplication with Matrix2x2.")

if __name__ == "__main__":
    pass