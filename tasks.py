"""Warehouse task definitions.

Coordinates use (row, column), with (0, 0) at the top-left corner.
"""
TASKS = [
    {"id": "T1", "position": (1, 10), "priority": 5, "deadline": 18},
    {"id": "T2", "position": (3, 13), "priority": 3, "deadline": 35},
    {"id": "T3", "position": (8, 2), "priority": 4, "deadline": 28},
    {"id": "T4", "position": (9, 11), "priority": 2, "deadline": 45},
]

CHARGER = (1, 2)
BATTERY_CAPACITY = 100
ENERGY_PER_STEP = 1
BATTERY_RESERVE = 8
