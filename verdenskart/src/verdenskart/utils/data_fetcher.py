"""Retrieve data for processing."""
from typing import Dict, Any, Iterable
import logging
import zipfile
import os

import requests
import fiona


SHAPES_SETS = {
    "coastline": "physical/ne_10m_coastline.zip",
    "location": "physical/ne_10m_geography_regions_polys.zip", # mountains, plates, etc.
    "country": "cultural/ne_10m_admin_0_countries.zip",
    "province": "cultural/ne_10m_admin_1_states_provinces.zip", # states, provinces, muncipalities, etc.
    "city": "cultural/ne_10m_populated_places.zip",
    "road": "cultural/ne_10m_roads.zip",
    "railroad": "cultural/ne_10m_railroads.zip",
    "urban": "cultural/ne_10m_urban_areas.zip", # area of dense population
    "timezone": "cultural/ne_10m_time_zones.zip",
    "disbuted": "cultural/ne_10m_admin_0_disputed_areas.zip", # breakaway/disputed areas
    "river": "physical/ne_10m_rivers_lake_centerlines.zip",
    "lake": "physical/ne_10m_lakes.zip",
    "reef": "physical/ne_10m_reefs.zip",
}


def get_world_topology() -> Dict[str, Any]:
    ans = requests.get("https://restcountries.eu/rest/v2/all?fields=name;capital;region;subregion;latlng;alpha2Code;alpha3Code;borders")
    if ans.status_code != 200:
        raise RuntimeError("Unable to get country data")
    countries = {country.pop("alpha3Code"): country for country in ans.json()}
    logging.info("Done getting raw topological data")
    return countries


def get_country_polygon(alpha2code: str) -> Dict[str, Any]:
    try:
        ans = requests.get("http://nominatim.openstreetmap.org/search?country={}&polygon_geojson=1&format=json".format(alpha2code.lower()))
        if ans.status_code != 200:
            raise RuntimeError("Unable to get boundary for {}".format(country))
        res = ans.json()
        if res:
            return res[0]["geojson"]
        else:
            print("Missing data for {}".format(alpha2code))
    except requests.exceptions.ChunkedEncodingError as err:
        print("Got error while getting polygon for".format(alpha2code))


def get_shapes(shape_set: str) -> Iterable[fiona.Collection]:
    """
    Retrieve shape data.

    Download content if needed.

    Args:
        shape_set:
            name of the shape set to retrieve. Valid values listed in
            `SHAPES_SETS` dict.

    Yields:
        Fiona collection; a dict-like object following the geoJSON structure.
    """
    logger = logging.getLogger(__name__)

    filename = SHAPES_SETS[shape_set]
    folder = os.path.join(
        os.path.expanduser("~"), ".cache", "world_domination", shape_set)
    filepath = os.path.join(folder, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # download if missing:
    if not os.path.isfile(filepath):
        logger.info("downloading missing dataset")

        ans = requests.get(
            "http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/{}".format(filename))
        if ans.status_code != 200:
            raise RuntimeError("Unable to get shape data")
        with open(filepath, "wb") as sink:
            sink.write(ans.content)

    with zipfile.ZipFile(filepath) as zipcontainer:

        # get shape filename:
        for filename in zipcontainer.namelist():
            if filename.endswith(".shp"):
                break

        # extract if just downloaded:
        if not os.path.isfile(os.path.join(folder, filename)):
            logger.info("extracting zip file")
            filenames = (
                filename for filename in zipcontainer.namelist()
                if filename[-4:] in (".shp", ".shx", ".prj")
            )
            for filename in filenames:
                with zipcontainer.open(filename) as filecontent:
                    filepath = os.path.join(folder, filename)
                    with open(filepath, "wb") as sink:
                        sink.write(filecontent.read())

        # get shape filename which fiona wants pointer to:
        for filename in zipcontainer.namelist():
            if filename.endswith(".shp"):
                break

    filepath = os.path.join(folder, filename)
    with fiona.open(filepath) as src:
        for element in src:
            yield element

for shape in get_shapes("reef"):
    print(shape)
