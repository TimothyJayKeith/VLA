#Imports
import numpy as np
from Spaces import Plane
from bokeh.io import show
from bokeh.models import Arrow, NormalHead

# Initialize standard plane to be used as default argument
standard_plane = Plane([[-10,10],[-10,10]])

def Place_Vector2D(vector, plane=standard_plane, start=[0,0], alpha=1.0):
    start = np.array(start)
    end = vector + start
    nh = NormalHead(line_color=vector.color, line_alpha=alpha, fill_color=vector.color, fill_alpha=alpha)
    plane.f.add_layout(Arrow(end=nh, x_start=start[0], y_start=start[1], x_end=end[0], y_end=end[1]))

def Graph(plane=standard_plane):
    show(plane.f)

if __name__ == "__main__":
    from Vectors import Vector2D
    vector = Vector2D([5,2])
    vector2 = Vector2D([1,-5], color="red")
    Place_Vector2D(vector)
    Place_Vector2D(vector, start=[1,2])
    Place_Vector2D(vector2, start=[-1,2])
    Graph()
