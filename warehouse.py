"""Warehouse grid loading and display."""
from pathlib import Path

WALL = "#"
OPEN = "."
START = "S"
PACKING = "P"


class Warehouse:
    def __init__(self, map_file):
        self.grid = [
            list(line.strip())
            for line in Path(map_file).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if not self.grid or any(len(row) != len(self.grid[0]) for row in self.grid):
            raise ValueError("Map must be a non-empty rectangular grid.")
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.start = self._find_one(START)
        self.packing = self._find_one(PACKING)

    def _find_one(self, symbol):
        found = [(r, c) for r in range(self.rows) for c in range(self.cols)
                 if self.grid[r][c] == symbol]
        if len(found) != 1:
            raise ValueError(f"Map must contain exactly one {symbol}.")
        return found[0]

    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_open(self, pos):
        return self.in_bounds(pos) and self.grid[pos[0]][pos[1]] != WALL

    def neighbors(self, pos, extra_blocked=None):
        extra_blocked = extra_blocked or set()
        r, c = pos
        for nxt in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if self.is_open(nxt) and nxt not in extra_blocked:
                yield nxt

    def display(self, robot=None, task_positions=None, collected=None, path=None):
        task_positions = task_positions or {}
        collected = collected or set()
        path = set(path or [])
        for r in range(self.rows):
            line = []
            for c in range(self.cols):
                p = (r, c)
                ch = self.grid[r][c]
                if p == robot:
                    ch = "R"
                elif p in task_positions and task_positions[p] not in collected:
                    ch = task_positions[p][-1]  # T1 -> 1
                elif p in path and ch == OPEN:
                    ch = "*"
                line.append(ch)
            print(" ".join(line))
