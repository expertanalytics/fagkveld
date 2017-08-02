"""
Data terrain model (DTM).

Examples::

    >>> from verdenskart import DTM
    >>> dtm = DTM()
    >>> print(dtm["NOR"])
    Location('Norway')
"""
from typing import Dict, List, Tuple, Set, Optional

from bokeh.models import Model
from bokeh.models import ColumnDataSource, Patches, LabelSet
import logging
import numpy as np

from .location import Location
from .coloring import set_location_colors
from ..utils.data_fetcher import get_world_topology, get_country_polygon



class DTM:

    locations: Location = {}
    data = None

    def __init__(self):

        # add countries:
        logging.info("Fetching topological data")
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

        # load norway
        norway = 'NO'
        coordinates = get_country_polygon(norway)
        self.locations['NOR'].border_x = []
        self.locations['NOR'].border_y = []
        for coords in coordinates['coordinates'][0]:
                co = np.array(coords)
                print(co)
                self.locations['NOR'].border_x.append(co[:, 0])
                self.locations['NOR'].border_y.append(co[:, 1])

        # add country colors
        self.set_location_colors()
        logging.info("Finshed __init__")

    def __getitem__(self, item):
        return self.locations[item]


    def set_location_colors(self):
        """Set color values on all locations and all location children."""
        for location in self.locations.values():
            if not location.color:
                set_location_colors(location)

    def visuals(self, level: Optional[int]=-1) -> List[Tuple[Model, ColumnDataSource]]:
        vis = []
        for location in self.locations.values():
            vis.extend(location.visuals(level))
        return vis

