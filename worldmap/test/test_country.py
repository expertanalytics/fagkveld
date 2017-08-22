import pytest
import numpy as np
import bokeh


@pytest.fixture()
def dtm():
    dtm = DTM()
    country1 = Country()
    country1.border_x = [np.array([1, 3, 3, 1])]
    country1.border_y = [np.array([0, 0, 1, 1])]

    country2 = Country()
    country2.border_x = [np.array([1, 3, 3, 1])]
    country2.border_y = [np.array([1, 1, 2, 2])]

    country3 = Country()
    country3.border_x = [np.array([0, 2, 2, 0])]
    country3.border_y = [np.array([2, 2, 3, 3])]

    country4 = Country()
    country4.border_x = [np.array([2, 4, 4, 2])]
    country4.border_y = [np.array([2, 2, 3, 3])]
    dtm.countries =  {
        "a": country1,
        "b": country2,
        "c": country3,
        "d": country4
    }
    return dtm

