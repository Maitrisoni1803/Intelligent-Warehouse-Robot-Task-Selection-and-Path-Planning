"""A* search with four interchangeable heuristics."""
import heapq
import math
from itertools import count


def heuristic(a, b, name):
    dr, dc = abs(a[0] - b[0]), abs(a[1] - b[1])
    if name == "manhattan":
        return dr + dc
    if name == "euclidean":
        return math.sqrt(dr * dr + dc * dc)
    if name == "chebyshev":
        return max(dr, dc)
    if name == "zero":
        return 0
    raise ValueError(f"Unknown heuristic: {name}")


def astar(warehouse, start, goal, heuristic_name="manhattan", extra_blocked=None):
    """Return (path, expanded_nodes). Path includes start and goal."""
    if start == goal:
        return [start], 0
    if not warehouse.is_open(goal):
        return [], 0

    tie = count()
    frontier = [(heuristic(start, goal, heuristic_name), 0, next(tie), start)]
    came_from = {}
    g_cost = {start: 0}
    closed = set()
    expanded = 0

    while frontier:
        _, current_g, _, current = heapq.heappop(frontier)
        if current in closed:
            continue
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, expanded

        closed.add(current)
        expanded += 1

        for nxt in warehouse.neighbors(current, extra_blocked):
            tentative = current_g + 1
            if tentative < g_cost.get(nxt, float("inf")):
                g_cost[nxt] = tentative
                came_from[nxt] = current
                f = tentative + heuristic(nxt, goal, heuristic_name)
                heapq.heappush(frontier, (f, tentative, next(tie), nxt))

    return [], expanded
