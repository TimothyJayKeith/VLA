#Imports
from bokeh.models import Range1d
from bokeh.plotting import figure

class Plane:
    """
    Plane on which graphing of vectors can be done.
    """
    def __init__(self, limits=[[-10,10],[-10,10]]):
        self.f = figure()
        self.f.x_range = Range1d(limits[0][0], limits[0][1])
        self.f.y_range = Range1d(limits[1][0], limits[1][1])
        self.f.axis.fixed_location = 0