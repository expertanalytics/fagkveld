
from typing import Dict, List, Tuple, Set, Optional
from abc import abstractmethod

import numpy

from bokeh.models import Model
from bokeh.models import ColumnDataSource, Patches, LabelSet


class Location:

    name: str = ""
    long_name: str = ""
    border_x: List[numpy.ndarray]
    border_hull_x: List[numpy.ndarray]
    border_y: List[numpy.ndarray] = []
    border_hull_y: List[numpy.ndarray] = []
    neighbors: "Locations" = {}
    parent: "Optional[Location]" = None
    children: "Locations" = {}
    level: int = 0
    alpha3code: str = ""
    color: str = ""

    border_ds_keys = ('xs', 'ys')
    border_ds = ColumnDataSource({k: [] for k in border_ds_keys})
    border_glyph = None

    location_ds_keys = ('name')
    location_ds = ColumnDataSource({k: [] for k in border_ds_keys})
    location_glyph = None

    def __init__(
            self,
            name: str,
            long_name: Optional[str] = None,
            parent: "Optional[Location]" = None,
    ):
        self.name = name
        self.long_name = long_name if long_name else name
        self.parent = parent
        self.border_x = []
        self.border_hull_x = []
        self.border_y = []
        self.border_hull_y = []

    @property
    def location_x(self) -> numpy.ndarray:
        pass
        # TODO: implement here

    @property
    def location_y(self) -> numpy.ndarray:
        pass
        # TODO: implement here

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
            line_alpha=0
        )

        vis.append((self.border_glyph, self.border_ds))
        # name at location x,y

        # child elements
        if level and (level > self.level or level == -1):
            for child in self.children.values():
                vis.extend(child.visuals(level))

        return vis

    def clear_visuals(self):
        self.border_ds.data = {k: [] for k in self.border_ds_keys}
        self.location_ds.data = {k: [] for k in self.border_ds_keys}

        for child in self.children.values():
            child.clear_visuals()

    def __str__(self):
        return "Location('{}')".format(self.long_name)


Locations = Dict[str, Location]

