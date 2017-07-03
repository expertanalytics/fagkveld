from typing import Dict, Any
import logging
import requests


def get_world_topology():
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


#if __name__ == "__main__":
#    topology = get_world_topology()
#    for c in topology.values():
#        c.pop("borders")
#        res = get_country_polygon(c["alpha2Code"])
