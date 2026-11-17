"""Run the warehouse robot simulation."""
from pathlib import Path
from warehouse import Warehouse
from agent import WarehouseAgent
from tasks import TASKS, CHARGER

ROOT = Path(__file__).resolve().parent


def main():
    warehouse = Warehouse(ROOT / "map.txt")
    task_positions = {t["position"]: t["id"] for t in TASKS}
    task_positions[CHARGER] = "CHARGER"

    print("\n=== INTELLIGENT WAREHOUSE ROBOT ===")
    print("Warehouse map: S=start, P=packing, #=shelf/wall, 1-4=tasks")
    warehouse.display(task_positions=task_positions)

    agent = WarehouseAgent(warehouse, heuristic_name="manhattan")
    result = agent.run()

    print("\n=== AGENT DECISION LOG ===")
    for item in result["log"]:
        print(item)

    print("\n=== FINAL RESULT ===")
    print(f"Tasks completed : {result['tasks_completed']}")
    print(f"Total distance  : {result['distance']} grid moves")
    print(f"Nodes expanded  : {result['expanded']}")
    print(f"Battery left    : {result['battery_remaining']}")
    print("\nSimulation completed successfully.")


if __name__ == "__main__":
    main()
