"""Warehouse reflex agent: task selection, navigation and delivery."""
from astar import astar
from tasks import (
    TASKS, CHARGER, BATTERY_CAPACITY, ENERGY_PER_STEP, BATTERY_RESERVE
)


class WarehouseAgent:
    def __init__(self, warehouse, heuristic_name="manhattan"):
        self.warehouse = warehouse
        self.heuristic_name = heuristic_name
        self.position = warehouse.start
        self.battery = BATTERY_CAPACITY
        self.collected = set()
        self.total_distance = 0
        self.total_expanded = 0
        self.log = []

    def _task_score(self, task):
        """Higher score is better. Deadline urgency and priority are rewarded."""
        path, _ = astar(
            self.warehouse, self.position, task["position"], self.heuristic_name
        )
        if not path:
            return float("-inf")
        distance = len(path) - 1
        urgency = 1 / max(task["deadline"], 1)
        # Transparent, simple scoring rule for this project.
        return (3 * task["priority"]) + (20 * urgency) - (0.5 * distance)

    def select_task(self):
        available = [t for t in TASKS if t["id"] not in self.collected]
        if not available:
            return None
        return max(available, key=self._task_score)

    def _follow_path(self, goal, label):
        path, expanded = astar(
            self.warehouse, self.position, goal, self.heuristic_name
        )
        self.total_expanded += expanded
        if not path:
            raise RuntimeError(f"No path found from {self.position} to {goal} ({label}).")

        steps = len(path) - 1
        required_energy = steps * ENERGY_PER_STEP

        # Reflex rule: recharge first if this trip would consume the reserve.
        if goal != CHARGER and self.battery < required_energy + BATTERY_RESERVE:
            self.log.append(
                f"REFLEX: battery {self.battery}; recharge before travelling to {label}."
            )
            self._follow_path(CHARGER, "charging station")
            self.battery = BATTERY_CAPACITY
            self.log.append("ACTION: battery recharged to full.")

        # Move one grid cell at a time and update battery.
        for next_pos in path[1:]:
            self.position = next_pos
            self.battery -= ENERGY_PER_STEP
            self.total_distance += 1

        self.log.append(
            f"ACTION: reached {label}; distance={steps}; battery={self.battery}."
        )

    def run(self):
        self.log.append(f"START: robot at {self.position}, battery={self.battery}.")
        task_by_id = {t["id"]: t for t in TASKS}

        while len(self.collected) < len(TASKS):
            task = self.select_task()
            if task is None:
                break
            self.log.append(
                f"DECISION: selected {task['id']} "
                f"(priority={task['priority']}, deadline={task['deadline']})."
            )
            self._follow_path(task["position"], task["id"])
            self.collected.add(task["id"])
            self.log.append(f"EVENT: {task['id']} collected.")

            self._follow_path(self.warehouse.packing, "packing station")
            self.log.append(f"EVENT: {task['id']} delivered to packing station.")

        self._follow_path(self.warehouse.start, "home/start")
        self.log.append("FINISH: all tasks delivered; robot returned to start.")
        return {
            "distance": self.total_distance,
            "expanded": self.total_expanded,
            "battery_remaining": self.battery,
            "tasks_completed": len(self.collected),
            "log": self.log,
        }
