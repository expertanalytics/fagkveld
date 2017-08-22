
import colorsys
import matplotlib.pyplot as plt

from descartes import PolygonPatch
from pprint import pprint

from .data_fetcher import get_shapes, SHAPES_SETS

BLUE = '#6699cc'
ORANGE = '#f98836'
PURPLE = '#c276cc'
GREEN = '#75cc7b'

def plotter() -> None:
    fig, ax = plt.subplots()

    c = {
            'norway': BLUE,
            'sweden': ORANGE,
            'denmark': PURPLE,
            'finland': GREEN
        }

    N = 275
    HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

    for i, shape in enumerate(get_shapes('country')):
        name = shape['properties']['NAME'].casefold()

        color = next(RGB_tuples)

        ax.add_patch(PolygonPatch(
            shape['geometry'], fc=color, ec=color, alpha=0.5))

    ax.set_aspect('equal', 'datalim')
    ax.relim()
    ax.autoscale_view()

    plt.show()


def main() -> None:
    plotter()

