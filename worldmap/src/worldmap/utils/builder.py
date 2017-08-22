"""
Location builder
"""
from typing import Dict, Type
import numpy

from .data_fetcher import get_shapes
from ..model.location import Location

HIERARKY = {
    "city": "country",
    "country": "continent",
}


def build_group(
        location_group: str,
        loction_class: Type[Location] = Location,
) -> Dict[str, Location]:
    """
    Build group (like country or cities).
    """
    groups = {}
    for shape in get_shapes(location_group):

        assert shape["type"] == "Feature"

        name = shape["properties"].get("ADMIN", location_group)

        location = location_class(name)

        location.alpha3code = shape["properties"].get("ADM0_A3")

        if location_group == "country":
            location.parent = shape["properties"]["CONTINENT"]
            location.level = 2

        elif location_group == "city":
            location.parent = shape["properties"]["ADM0NAME"]
            location.level = 3

        if shape["geometry"]["type"] in ("LineString", "Polygon"):

            coordinates = numpy.array(shape["geometry"]["coordinates"])
            location.border_x.append(coordinates.T[0])
            location.border_y.append(coordinates.T[1])

        location.shape = shape
        groups[name] = location

    return groups


def build_coastlines(loction_class: Type[Location] = Location):
    return build_group("coastline", loction_class)

def build_countries(loction_class: Type[Location] = Location):
    return build_group("country", loction_class)

def build_cities(loction_class: Type[Location] = Location):
    return build_group("city", loction_class)
