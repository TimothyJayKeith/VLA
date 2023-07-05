#Imports
from bokeh.models import Range1d
from bokeh.plotting import figure

class Plane:
    """
    Plane on which graphing of vectors can be done.
    """
    def __init__(self, limits=None):
        self.f = figure()
        if limits is not None:
            self.f.x_range = Range1d(limits[0][0], limits[0][1])
            self.f.y_range = Range1d(limits[1][0], limits[1][1])