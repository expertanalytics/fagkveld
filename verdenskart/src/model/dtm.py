from typing import Dict, Set
import numpy

from model import location

class DTM:

    countries: location.Countries = {}
    data = None

    def get_visuals(self):
        pass