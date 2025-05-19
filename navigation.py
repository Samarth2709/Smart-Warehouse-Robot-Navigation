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


def find_shortest_path(grid: Grid, start: Coord, goal: Coord) -> List[Coord]:
    """Return a list of coordinates from *start* to *goal* inclusive.

    The path **must**:
    * move only up / down / left / right (no diagonals)
    * avoid `#` obstacle cells
    * start == path[0], goal == path[-1]

    Feel free to implement A*, Dijkstra, BFS, etc.
    """
    raise NotImplementedError("Path‑finding algorithm not yet implemented")
