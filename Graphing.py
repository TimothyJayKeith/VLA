#Imports
import numpy as np
import Vectors
from Spaces import Plane
from bokeh.io import show
from bokeh.models import Arrow, NormalHead

# Initialize standard plane to be used as default argument
standard_plane = Plane([[-10,10],[-10,10]])

def Place_Vector2D(vector, plane=standard_plane, start=[0,0], alpha=1.0):
    start = np.array(start)
    end = vector + start
    nh = NormalHead(line_color=vector.color, line_alpha=alpha, fill_color=vector.color, fill_alpha=alpha)
    plane.f.add_layout(Arrow(end=nh, line_color=vector.color, line_alpha=alpha, line_width=3,
                             x_start=start[0], y_start=start[1], x_end=end[0], y_end=end[1]))

    return end

def Place(object, plane=standard_plane, start=[0, 0], alpha=1.0, show_components=True):
    if type(object) == Vectors.Vector2D:
        Place_Vector2D(object, plane, start, alpha)
        if show_components and len(object._components) > 1:
            for component in object._components:
                start = Place_Vector2D(component, plane, start, alpha=.2*alpha)

def Graph(plane=standard_plane):
    show(plane.f)

if __name__ == "__main__":
    vector1 = Vectors.Vector2D([3,2], color="blue")
    vector2 = Vectors.Vector2D([-4,-5], color="red")
    vector3 = Vectors.Vector2D([-5, 7], color="green")
    Place(vector1 + vector2 + vector3, start=[2,1])
    Graph()
