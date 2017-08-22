from typing import Dict, List, Tuple, Set, Optional
from abc import abstractmethod

import numpy


class Location:

    name: str = ""
    long_name: str = ""
    border_x: List[numpy.ndarray] = []
    border_hull_x: List[numpy.ndarray] = []
    border_y: List[numpy.ndarray] = []
    border_hull_y: List[numpy.ndarray] = []
    neighbors: "Locations" = {}
    parent: "Optional[Location]" = None
    children: "Locations" = {}
    level: int = 0
    alpha3code: str = ""
    color: str = ""

    def __init__(self, name: str, long_name: Optional[str]=None, Location: Optional[parent]=None):
        self.name = name
        if long_name:
            self.long_name = long_name
        else:
            self.long_name = name

    @property
    def location_x(self) -> float:
        pass
        # TODO: implement here

    @property
    def location_y(self) -> float:
        pass
        # TODO: implement here

    def __str__(self):
        return "Location('{}')".format(self.long_name)


Locations = Dict[str, Location]
