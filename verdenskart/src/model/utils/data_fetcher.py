import logging
import requests


def get_world_topology():
    ans = requests.get("https://restcountries.eu/rest/v2/all?fields=name;capital;region;subregion;latlng;alpha3Code;borders")
    if ans.status_code != 200:
        raise RuntimeError("Unable to get country data")
    countries = {country.pop("alpha3Code"): country for country in ans.json()}
    logging.info("Done getting raw topological data")
    return countries
