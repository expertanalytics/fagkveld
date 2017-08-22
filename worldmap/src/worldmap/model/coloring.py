"""
Set color values to all locations
"""

from ..utils.colors_hybrid import COLORS
from .location import Location


def set_location_colors(location: Location):
    """
    Set color values on all locations and all location children.

    Follows the rule that a location can not have the same colors as any
    neighbors or any parents.

    **In-place change `location.color`**

    Args:
        location: The root location to set color.
    """
    colors = set(COLORS.values())

    # define neighboring and parental colors:
    neighbor_colors = {
        neighbor.color for neighbor in location.neighbors.values()
        if neighbor.color
    }
    parent = location.parent
    while parent:
        neighbor_colors.add(location.parent.color)
        parent = parent.parent

    location.color = colors.difference(neighbor_colors).pop()

    # add colors to all children:
    for child in location.children.values():
        if not child.color:
            set_location_colors(child)

