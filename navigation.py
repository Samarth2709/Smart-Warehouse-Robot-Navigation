"""
Provide a function `find_shortest_path` that returns the *shortest* valid
path between two coordinates on the grid.  The starter kit raises
`NotImplementedError` so the test suite will `xfail` until you fill it in.

You may import any standard‑library modules but **no third‑party** libs.
You may also add helper functions/classes below.
"""
from __future__ import annotations

from typing import List, Tuple

Coord = Tuple[int, int]  # (row, col)
Grid = List[List[str]]

__all__ = ["find_shortest_path"]


def find_shortest_path(grid: Grid, start_coord: Coord, pickup_coord: Coord, dropoff_coord: Coord) -> List[Coord]:
    """Return a list of coordinates representing the path: start_coord -> pickup_coord -> dropoff_coord.

    The path **must**:
    * move only up / down / left / right (no diagonals)
    * avoid `#` obstacle cells
    * start_coord == path[0], pickup_coord should be in the path, and dropoff_coord == path[-1]

    Implement A* search to find the shortest path.
    The returned path should be a single list of coordinates, e.g.
    [start_coord, ..., pickup_coord, ..., dropoff_coord].
    """
    raise NotImplementedError("Path‑finding algorithm not yet implemented")
