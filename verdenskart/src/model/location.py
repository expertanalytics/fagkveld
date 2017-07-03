from typing import Dict, List, Tuple, Set
from abc import abstractmethod

import numpy

from bokeh.models import Model
from bokeh.models import ColumnDataSource

class Location:
    """"""

    name: str = ""
    border_x: List[numpy.ndarray] = []
    border_hull_x: List[numpy.ndarray] = []
    border_y: List[numpy.ndarray] = []
    border_hull_y: List[numpy.ndarray] = []

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
        pass
        # TODO: implement here


class Country(Location):

    neighbors: "Countries" = {}
    cities: "Cities" = {}
    color: str

Countries = Dict[str, Country]


class City(Location):

    country: Country

Cities = Dict[str, City]
