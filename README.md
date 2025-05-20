# Smart Warehouse Robot Navigation — Starter Kit

This repository contains starter code for the **Smart Warehouse Robot Navigation** assignment.  It gives you everything you need except the path‑finding logic (that's your job).

---

## Project Brief

Write an algorithm that lets a robot move through a 2‑D grid warehouse:

1. From **Start** `S` ➔ **Pickup** `P`
2. From **Pickup** `P` ➔ **Drop‑off** `D`

The robot must avoid obstacles `#` and stay on empty tiles `.` while taking the *shortest* valid route.

---

## Repository Structure

```
.
├── grid.py            # Generates random N×M grids with S / P / D / obstacles
├── navigation.py      # ←––– Implement your path‑finding here (A*, Dijkstra, BFS, …)
├── validator.py       # Utility to check whether a path is valid
├── test_navigation.py # Pytest harness that runs the validator on your solution
└── README.md          # You are here
```

---

## Getting Started

### 1  Install Python ≥ 3.9

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -U pytest
```

### 2  Generate a grid & view it

```python
>>> from grid import generate_grid, print_grid
>>> g, S, P, D = generate_grid(rows=8, cols=12, obstacle_prob=0.25, seed=42)
>>> print_grid(g)
```

### 3  Implement `find_shortest_path` in **navigation.py**

Open `navigation.py` and replace the `raise NotImplementedError` line with your own code.
Your function should accept the grid, start (S), pickup (P), and drop-off (D) coordinates and return a single list of coordinates representing the path from S to P, and then P to D.
Your immplementation should return an empty list if there exists no Manhattan path from S to P to D. 

### 4  Run the tests

```bash
pytest -q        # prints `1 passed` if your paths are valid
```
These cases are not comprehensive tests for your implementation. 
This only verifies if the path is valid for a grid which gaurantees a valid path exists.

---

## Deliverables

Submit **only** these files:

* `navigation.py`  ← your algorithm
* (optionally) any helper modules you create, as long as they import cleanly

Tests **must pass** on an unseen random grid (`pytest`).  Do **not** modify `grid.py`, `validator.py`, or the test harness.

---

## Rules & Tips

* The grid uses **4‑neighbour (Manhattan)** moves (no diagonals).
* A* with an admissible Manhattan‑distance heuristic is recommended.
* Your path should start at S, go through P, and end at D. The list of coordinates should represent this entire journey.
