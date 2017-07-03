from typing import Dict, Set
import numpy

from model.location import Locations
from model.coloring import set_location_colors

class DTM:

    locations: Locations = {}
    data = None

    def set_loction_colors(self):
        """Set color values on all locations and all location children."""
        for location in self.locations:
            if not location.color:
                set_location_colors(location)


    def visuals(self):
        pass