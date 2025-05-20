"""
Utilities to verify that a candidate path satisfies all rules.

Usage
-----
>>> from grid import generate_grid
>>> from validator import is_valid_path
>>> g, S, P, D = generate_grid(8, 8, seed=0)
>>> candidate = [S, ..., P]
>>> assert is_valid_path(g, S, P, candidate)
"""
from typing import List, Tuple

Coord = Tuple[int, int]
Grid = List[List[str]]


def is_adjacent(a: Coord, b: Coord) -> bool:
    """True iff *a* and *b* share an edge (Manhattan)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def is_valid_path(grid: Grid, start: Coord, pickup: Coord, dropoff: Coord, path: List[Coord]) -> bool:
    """Return True if *path* obeys all constraints for S -> P -> D.

    Constraints
    -----------
    1. Non‑empty; first == start; last == dropoff; pickup is in path
    2. Stays inside bounds
    3. Moves only one step 4‑directionally at a time
    4. Does not step on obstacle cells ("#")
    """
    if not path:
        return False
    if path[0] != start or path[-1] != dropoff:
        return False
    if pickup not in path:
        return False
    if len(path) < 3:
        return False
    
    # Pickup should never equal start or dropoff
    if pickup == start or pickup == dropoff:
        return False
    
    pickup_index = path.index(pickup)
    # Make sure the index of pickup is between 0 and len(path)-1
    if pickup_index < 0 or pickup_index >= len(path):
        return False

    rows, cols = len(grid), len(grid[0])

    for idx, coord in enumerate(path):
        r, c = coord
        # Bounds check
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        # Obstacle check
        if grid[r][c] == "#":
            return False
        # Move check (skip first element)
        if idx > 0 and not is_adjacent(path[idx - 1], coord):
            return False

    return True