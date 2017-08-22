
from bokeh.plotting import output_file, figure, show, curdoc
from bokeh.layouts import row, column, layout, widgetbox, Spacer
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, Panel, Tabs
from bokeh.client import push_session
import numpy as np
from typing import Dict, List, Tuple, Set, Optional

from worldmap.model.dtm import DTM

import logging


locations = None

fig = figure()

# add glyphs

def visuals(self, locations, level: Optional[int] = -1) -> List[Tuple[Model, ColumnDataSource]]:
    vis = []
    for location in locations.values():
        vis.extend(location.visuals(level))
    return vis

for (glyph, data_source) in visuals(locations, level=-1):
    if data_source.data:
        fig.add_glyph(data_source, glyph=glyph)
        logging.debug(data_source.data)

curdoc().add_root(fig)

