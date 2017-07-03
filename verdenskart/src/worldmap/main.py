from bokeh.plotting import output_file, figure, show, curdoc
from bokeh.layouts import row, column, layout, widgetbox, Spacer
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, Panel, Tabs
from bokeh.client import push_session
import numpy as np

from model.dtm import DTM

dtm = DTM()
fig = figure()

# add glyphs
for (glyph, data_source) in dtm.visuals(level=-1):
    fig.add_glyph(glyph=glyph, data_source=data_source)

curdoc().add_root(fig)
