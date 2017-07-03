from bokeh.plotting import output_file, figure, show, curdoc
from bokeh.layouts import row, column, layout, widgetbox, Spacer
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, Panel, Tabs
from bokeh.client import push_session
import numpy as np

from verdenskart.model import DTM

def create_dtm():
    dtm = DTM()
    country1 = Country()
    country1.border_x = [np.array([1, 3, 3, 1])]
    country1.border_y = [np.array([0, 0, 1, 1])]

    country2 = Country()
    country2.border_x = [np.array([1, 3, 3, 1])]
    country2.border_y = [np.array([1, 1, 2, 2])]

    country3 = Country()
    country3.border_x = [np.array([0, 2, 2, 0])]
    country3.border_y = [np.array([2, 2, 3, 3])]

    country4 = Country()
    country4.border_x = [np.array([2, 4, 4, 2])]
    country4.border_y = [np.array([2, 2, 3, 3])]
    dtm.countries =  {
        "a": country1,
        "b": country2,
        "c": country3,
        "d": country4
    }
    return dtm


dtm = DTM()

fig = figure()

# add glyphs
for glyph, data_source in dtm.get_visuals():
    fig.add_glyph(glyph=glyph, data_source=data_source)

curdoc().add_root(fig)
