#Imports
import numpy as np
import Vectors
import Spaces
import Objects
from bokeh.io import show
from bokeh.models import Arrow, NormalHead

# Initialize standard plane to be used as default argument
standard_plane = Spaces.Plane()

def Place_Vector2D(vector, plane=standard_plane, start=[0,0], alpha=1.0):
    start = np.array(start)
    end = vector + start
    if np.allclose(vector.coordinates, np.zeros(2)):
        plane.f.circle_dot(start[0], start[1], size=6, color=vector.color, alpha=alpha)
    else:
        nh = NormalHead(line_color=vector.color, line_alpha=alpha, fill_color=vector.color, fill_alpha=alpha)
        plane.f.add_layout(Arrow(end=nh, line_color=vector.color, line_alpha=alpha, line_width=3,
                                x_start=start[0], y_start=start[1], x_end=end[0], y_end=end[1]))

    return end

def Place(object, plane=standard_plane, start=[0, 0], alpha=1.0, show_components=True):
    if type(object) == Vectors.Vector2D:
        Place_Vector2D(object, plane, start, alpha)
        if show_components:
            for component in object._components:
                start = Place_Vector2D(component, plane, start, alpha=.2*alpha)
    
    if type(object) == Objects.Circle:
        x = np.array([object.radius * np.cos(2*np.pi * i/128) for i in range(129)]) + start[0]
        y = np.array([object.radius * np.sin(2*np.pi * i/128) for i in range(129)]) + start[1]
        plane.f.line(x, y, alpha=alpha, color=object.color)
        if show_components:
            for component in object.center._components:
                start = Place_Vector2D(component, plane, start, alpha=.2*alpha)
    
    if isinstance(object, Objects.PGraph2D):
        delta = (plane.domain[1] - plane.domain[0])/128
        x = np.array([object.f1(plane.domain[0] + i*delta) for i in range(129)]) + start[0]
        y = np.array([object.f2(plane.domain[0] + i*delta) for i in range(129)]) + start[1]
        plane.f.line(x, y, alpha=alpha, color=object.color)
    
    if type(object) == Objects.Polygon:
        for i in range(len(object.vertices)):
            if i < len(object.vertices) - 1:
                plane.f.segment(object.vertices[i, 0], object.vertices[i, 1], 
                                object.vertices[i + 1, 0], object.vertices[i + 1, 1], color=object.color, width=1.5)
            else:
                plane.f.segment(object.vertices[i, 0], object.vertices[i, 1],
                                object.vertices[0, 0], object.vertices[0, 1], color=object.color, width=1.5)

def Graph(space=standard_plane):
    show(space.f)

if __name__ == "__main__":
    triangle = Objects.Polygon([[0, 0], [2, 0], [1, 1]])
    Place(triangle)
    Graph()
