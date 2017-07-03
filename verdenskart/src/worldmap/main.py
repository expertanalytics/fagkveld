from bokeh.plotting import output_file, figure, show, curdoc
from bokeh.layouts import row, column, layout, widgetbox, Spacer
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, Panel, Tabs
from bokeh.client import push_session
import numpy as np

from verdenskart.model import DTM


fig = figure()

dtm = None

# add glyphs
for glyph, data_source in dtm.visuals():
    fig.add_glyph(glyph=glyph, data_source=data_source)

curdoc().add_root(fig)
