from typing import Dict, List, Tuple, Set, Optional
from abc import abstractmethod

import numpy

from bokeh.models import Model
from bokeh.models import ColumnDataSource, Patches, LabelSet


class Location:

    name: str = ""
    border_x: List[numpy.ndarray] = []
    border_hull_x: List[numpy.ndarray] = []
    border_y: List[numpy.ndarray] = []
    border_hull_y: List[numpy.ndarray] = []
    neighbors: "Locations" = {}
    parent: "Optional[Location]" = None
    children: "Locations" = {}
    level: int = 0

    # bokeh
    border_ds_keys = ('xs', 'ys')
    border_ds = ColumnDataSource({k: [] for k in border_ds_keys})
    border_glyph = None

    location_ds_keys = ('name')
    location_ds = ColumnDataSource({k: [] for k in border_ds_keys})
    location_glyph = None


    @property
    def location_x(self) -> float:
        pass
        # TODO: implement here

    @property
    def location_y(self) -> float:
        pass
        # TODO: implement here

    @property
    @abstractmethod
    def visuals(self) -> List[Tuple[Model, ColumnDataSource]]:
        # border
        self.border_ds = ColumnDataSource({'xs': self.border_x,
                                           'ys': self.border_y})
        self.border_glyph = Patches(xs='xs', ys='ys', source=self.border_ds)

        # name at location x,y

        return [(self.border_glyph, self.border_ds)]

    @property
    def clear_visuals(self):
        self.border_ds.data = {k: [] for k in self.border_ds_keys}
        self.location_ds.data = {k: [] for k in self.border_ds_keys}

Locations = Dict[str, Location]
