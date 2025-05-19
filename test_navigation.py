"""
Pytest harness that validates the user's `find_shortest_path` implementation.

Run `pytest -q` in the repository root.  The test is marked *xfail* until
`navigation.py` is implemented.
"""
import pytest

from grid import generate_grid
from navigation import find_shortest_path
from validator import is_valid_path


@pytest.mark.parametrize("rows, cols, seed", [(8, 12, 0), (10, 15, 1), (12, 20, 2)])
def test_pathfinding(rows, cols, seed):
    grid, start, pickup, dropoff = generate_grid(rows, cols, obstacle_prob=0.25, seed=seed)

    try:
        # Leg 1: S ➔ P
        path1 = find_shortest_path(grid, start, pickup)
        assert is_valid_path(grid, start, pickup, path1)

        # Leg 2: P ➔ D
        path2 = find_shortest_path(grid, pickup, dropoff)
        assert is_valid_path(grid, pickup, dropoff, path2)
    except NotImplementedError:
        pytest.xfail("Path‑finding not yet implemented")
