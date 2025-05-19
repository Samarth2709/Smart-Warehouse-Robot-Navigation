"""
Utility for generating and pretty‑printing random warehouse grids.

Legend
------
S : Start cell (single)
P : Pickup cell (single)
D : Drop‑off cell (single)
# : Obstacle / shelf (impassable)
. : Empty floor (passable)
"""
from __future__ import annotations

import sys
import random
from enum import Enum
from typing import List, Tuple, Optional

class Cell(str, Enum):
    EMPTY = "."
    OBSTACLE = "#"
    START = "S"
    PICKUP = "P"
    DROPOFF = "D"

Grid = List[List[str]]
Coord = Tuple[int, int]  # row, col

__all__ = [
    "Cell",
    "Grid",
    "Coord",
    "generate_grid",
    "print_grid",
]


def _random_empty_cell(grid: Grid) -> Coord:
    """Return a random coordinate whose current value is EMPTY."""
    rows, cols = len(grid), len(grid[0])
    while True:
        r, c = random.randrange(rows), random.randrange(cols)
        if grid[r][c] == Cell.EMPTY:
            return r, c


def generate_grid(
    rows: int,
    cols: int,
    obstacle_prob: float = 0.20,
    seed: Optional[int] = None,
) -> Tuple[Grid, Coord, Coord, Coord]:
    """Create a random grid and return (grid, start, pickup, dropoff).

    The function **guarantees** that S, P, and D are placed on distinct
    empty cells but does *not* guarantee global path connectivity. Your
    algorithm should be able to report failure if no path exists.
    """
    if not 0 <= obstacle_prob <= 1:
        raise ValueError("obstacle_prob must be in [0, 1]")

    if rows * cols < 3:
        raise ValueError("Grid must be large enough to place S, P, and D (at least 3 cells)")

    if seed is not None:
        random.seed(seed)

    # 1. Fill with empty floor
    grid: Grid = [[Cell.EMPTY.value for _ in range(cols)] for _ in range(rows)]

    # 2. Place S, P, D on distinct empty cells
    start = _random_empty_cell(grid)
    grid[start[0]][start[1]] = Cell.START.value

    pickup = _random_empty_cell(grid)
    grid[pickup[0]][pickup[1]] = Cell.PICKUP.value

    dropoff = _random_empty_cell(grid)
    grid[dropoff[0]][dropoff[1]] = Cell.DROPOFF.value

    # 3. Sprinkle obstacles on remaining empty cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == Cell.EMPTY.value: # Only consider placing obstacles on empty cells
                if random.random() < obstacle_prob:
                    grid[r][c] = Cell.OBSTACLE.value

    return grid, start, pickup, dropoff


def print_grid(grid: Grid) -> None:
    """Pretty‑print the grid to stdout."""
    for row in grid:
        print(" ".join(row))


if __name__ == "__main__":
    # Get m and n from CLI arguments
    if len(sys.argv) != 3:
        print("Usage: python grid.py <m> <n>")
        sys.exit(1)
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    g, s, p, d = generate_grid(n, m, obstacle_prob=0.25)
    print_grid(g)
