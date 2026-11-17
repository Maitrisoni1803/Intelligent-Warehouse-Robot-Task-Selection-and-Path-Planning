"""Compare four A* heuristics on identical warehouse routes."""
from pathlib import Path
import csv
import time
from astar import astar
from warehouse import Warehouse
from tasks import TASKS

ROOT = Path(__file__).resolve().parent
HEURISTICS = ["manhattan", "euclidean", "chebyshev", "zero"]


def main():
    warehouse = Warehouse(ROOT / "map.txt")
    start = warehouse.start
    goals = [t["position"] for t in TASKS] + [warehouse.packing]

    rows = []
    print("\n=== A* HEURISTIC COMPARISON ===")
    print(f"{'Heuristic':<14}{'Route':<12}{'Path cost':<12}{'Expanded':<12}{'Time (ms)':<12}")

    for name in HEURISTICS:
        total_cost = 0
        total_expanded = 0
        total_ms = 0.0
        current = start

        for goal in goals:
            t0 = time.perf_counter()
            path, expanded = astar(warehouse, current, goal, name)
            elapsed = (time.perf_counter() - t0) * 1000
            if not path:
                raise RuntimeError(f"No path for {name}: {current} -> {goal}")
            cost = len(path) - 1
            total_cost += cost
            total_expanded += expanded
            total_ms += elapsed
            current = goal

        rows.append({
            "heuristic": name,
            "total_path_cost": total_cost,
            "nodes_expanded": total_expanded,
            "execution_time_ms": round(total_ms, 4),
        })
        print(f"{name:<14}{'all goals':<12}{total_cost:<12}{total_expanded:<12}{total_ms:<12.4f}")

    output = ROOT / "heuristic_comparison.csv"
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved results to: {output.name}")
    print("Note: execution time can vary between runs and computers.")


if __name__ == "__main__":
    main()
