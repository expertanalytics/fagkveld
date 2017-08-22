from typing import Dict, List, Tuple, Set, Optional
from bokeh.models import Model
from bokeh.models import ColumnDataSource, Patches, LabelSet

from .location import Location


class BokehLocation(Location):

    def __init__(self, name):
        super().__init__(name)

        self.border_ds_keys = ('xs', 'ys')
        self.border_ds = ColumnDataSource({k: [] for k in self.border_ds_keys})
        self.border_glyph = None

        self.location_ds_keys = ('name')
        self.location_ds = ColumnDataSource({k: [] for k in self.border_ds_keys})
        self.location_glyph = None

    def visuals(self, level: Optional[int]) -> List[Tuple[Model, ColumnDataSource]]:

        vis = []
        # border

        self.border_ds = ColumnDataSource({'xs': self.border_x,
                                           'ys': self.border_y})
        color = self.color if self.color else 'blue'
        self.border_glyph = Patches(
            xs='xs',
            ys='ys',
            fill_color=color,
            line_color=color,
            line_alpha=0,
        )
        self.border_ds.on_change('selected', self.on_click)

        vis.append((self.border_glyph, self.border_ds))
        # name at location x,y
        # child elements
        if level and (level > self.level or level == -1):
            for child in self.children.values():
                vis.extend(child.visuals(level))

        return vis

    def on_click(self, attr, old, new):
        print(" I was clicked and my name is {}".format(self.long_name))

    def clear_visuals(self):
        self.border_ds.data = {k: [] for k in self.border_ds_keys}
        self.location_ds.data = {k: [] for k in self.border_ds_keys}

        for child in self.children.values():
            child.clear_visuals()
