from typing import Dict, Set
import numpy

from model import location
from utils.colors_hybrid import  COLORS

class DTM:

    countries: location.Countries = {}
    data = None

    def get_neighbors(self, country: str) -> location.Countries:
        pass
        # TODO: implement here

    def set_country_colors(self):

        colors = set(COLORS.values())
        for country in self.countries.values():
            neighbor_colors = {
                neighbor.color for neighbor in country.neighbors.values()
                if neighbor.color
            }
            country.color = colors.difference(neighbor_colors).pop()
