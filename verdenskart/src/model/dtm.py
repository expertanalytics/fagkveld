from typing import Dict, List, Tuple, Set, Optional
import numpy

from bokeh.models import Model
from bokeh.models import ColumnDataSource, Patches, LabelSet

from .location import Location
from .coloring import set_location_colors
from .utils.data_fetcher import get_world_topology


class DTM:

    locations: Location = {}
    data = None

    def __init__(self):

        # add countries:
        countries = get_world_topology()
        for name, country in countries.items():
            self.locations[name] = Location(
                name=name, long_name=country["name"])

        # add country neighbors:
        for name, country in countries.items():
            self.locations[name].neighbors = {
                neighbor: self.locations[neighbor]
                for neighbor in country["borders"]
            }

        # add country colors
        self.set_location_colors()

    def set_location_colors(self):
        """Set color values on all locations and all location children."""
        for location in self.locations.values():
            if not location.color:
                set_location_colors(location)

    def visuals(self, level: Optional(int)=-1) -> List[Tuple[Model, ColumnDataSource]]:
        vis = []
        for location in self.locations.values():
            vis.extend(location.visuals(level))
        return vis