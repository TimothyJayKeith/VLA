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

class Line:
    def __init__(self, limits=[-10,10]) -> None:
        self.f = figure()
        self.f.x_range = Range1d(limits[0], limits[1])
        self.f.y_range = Range1d(-1,1)
        self.f.xaxis.fixed_location = 0
        self.f.xaxis.axis_line_color = "black"

        self.f.yaxis.axis_line_color = None
        self.f.yaxis.major_label_text_color = None
        self.f.yaxis.major_tick_line_color = None
        self.f.yaxis.minor_tick_line_color = None
        self.f.frame_height = 100