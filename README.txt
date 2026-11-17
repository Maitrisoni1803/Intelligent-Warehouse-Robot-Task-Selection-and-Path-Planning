# 🤖 Intelligent Warehouse Robot – Task Selection and Path Planning

### AI-Based Warehouse Automation Using A* Search Algorithm

<p align="center">
  <strong>An Intelligent Robot Simulation for Automated Task Selection, Optimal Path Planning, Obstacle Avoidance, and Battery Management.</strong>
</p>

---

## 📌 1. Project Overview

The **Intelligent Warehouse Robot – Task Selection and Path Planning** project is a Python-based simulation that demonstrates how an autonomous robot can perform tasks efficiently inside a warehouse environment.

In a warehouse, robots need to identify tasks, select which task to perform, navigate through different locations, avoid obstacles, and manage their battery levels.

This project uses **Artificial Intelligence (AI)** techniques and the **A* Search Algorithm** to help a robot make intelligent decisions and find suitable paths.

The simulation includes a grid-based warehouse, task prioritization, path planning, battery monitoring, a charging station, and a graphical user interface.

## 🎯 2. Project Objectives

- Develop an intelligent warehouse robot simulation using Python.
- Implement automatic task selection based on priority, urgency, and distance.
- Apply the A* search algorithm for path planning.
- Compare different heuristic functions.
- Enable obstacle avoidance during robot movement.
- Monitor battery consumption and charging requirements.
- Visualize robot movement through a graphical user interface.

## ✨ 3. Key Features

| Feature | Description |
|---|---|
| **Intelligent Task Selection** | Selects tasks using priority, deadline urgency, and distance. |
| **A* Path Planning** | Finds a path from the robot's current position to its destination. |
| **Obstacle Avoidance** | Prevents the robot from moving through blocked warehouse cells. |
| **Heuristic Comparison** | Compares Manhattan, Euclidean, Chebyshev, and Zero heuristics. |
| **Battery Management** | Tracks battery consumption during robot movement. |
| **Charging Station** | Allows the robot to recharge when required. |
| **Graphical Interface** | Displays the warehouse and robot simulation visually. |
| **Performance Analysis** | Compares path cost, expanded nodes, and execution time. |

## 🛠️ 4. Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Main programming language |
| **A* Search Algorithm** | Intelligent pathfinding |
| **Heuristic Functions** | Estimate distance to the destination |
| **Tkinter** | Graphical user interface |
| **CSV** | Store heuristic comparison results |
| **Jupyter Notebook** | Interactive execution and experimentation |
| **Visual Studio Code** | Development environment |
| **GitHub** | Project hosting and version control |

## 🧠 5. Algorithms and Methodology

### 5.1 A* Search Algorithm

A* is an informed search algorithm used to find an efficient path between two points.

It calculates the estimated total cost using:

**f(n) = g(n) + h(n)**

Where:

- **g(n):** Actual cost from the starting point to the current node.
- **h(n):** Estimated cost from the current node to the destination.
- **f(n):** Estimated total path cost.

### 5.2 Heuristic Functions

The project compares four heuristic functions:

| Heuristic | Description |
|---|---|
| **Manhattan Distance** | Calculates distance using horizontal and vertical movements. |
| **Euclidean Distance** | Calculates straight-line distance between two points. |
| **Chebyshev Distance** | Calculates distance using the maximum coordinate difference. |
| **Zero Heuristic** | Uses zero as the estimated remaining cost, similar to Dijkstra's algorithm. |

### 5.3 Intelligent Task Selection

The robot selects tasks based on three important factors:

1. **Priority:** Importance of the task.
2. **Deadline Urgency:** How soon the task needs to be completed.
3. **Distance:** How far the robot is from the task location.

The task-selection logic uses a configurable scoring rule to decide which task should be performed.

### 5.4 Battery Management

The robot starts with a battery capacity of **100 units**.

- Each movement consumes one battery unit.
- The robot monitors its remaining battery.
- A reserve battery level is maintained.
- The robot considers the charging station when its battery is insufficient for the planned journey.

## 🔄 6. Project Workflow

The following flowchart represents the overall working process of the warehouse robot.

```mermaid
flowchart TD
    A([Start]) --> B[Load Warehouse Grid]
    B --> C[Initialize Robot and Battery]
    C --> D[Load Available Tasks]
    D --> E{Tasks Available?}
    E -- No --> K[Display Final Results]
    E -- Yes --> F[Calculate Task Scores]
    F --> G[Select Best Task]
    G --> H[Check Battery Level]
    H --> I{Battery Sufficient?}
    I -- No --> J[Navigate to Charging Station]
    J --> L[Recharge Battery]
    L --> M[Plan Path Using A*]
    I -- Yes --> M
    M --> N[Avoid Obstacles and Move]
    N --> O[Reach Task Location]
    O --> P[Complete Task]
    P --> Q[Update Battery and Task Status]
    Q --> E
    K --> R([End])
```

## 📂 7. Project Folder Structure

The repository contains the following files:

| File Name | Description |
|---|---|
| `main.py` | Runs the complete warehouse robot simulation. |
| `gui.py` | Provides the graphical warehouse simulation. |
| `warehouse.py` | Loads and represents the warehouse grid. |
| `agent.py` | Implements robot decision-making and task selection. |
| `astar.py` | Implements the A* pathfinding algorithm and heuristics. |
| `tasks.py` | Stores task information, battery settings, and charger details. |
| `compare_heuristics.py` | Compares the performance of different heuristic functions. |
| `compare_heuristics (1).ipynb` | Jupyter Notebook for interactive heuristic comparison. |
| `map.txt` | Contains the warehouse grid layout. |
| `heuristic_comparison.csv` | Stores heuristic comparison results. |
| `README.md` | Project documentation. |

## ⚙️ 8. Installation and Setup

### Prerequisites

Before running the project, make sure you have:

- Python 3.9 or newer
- Visual Studio Code
- Python extension for VS Code

**Note:** The main simulation uses Python's standard library. Tkinter is included with many Python installations. No additional pip packages are required for the basic simulation.

### Step 1: Clone the Repository

Open the terminal and execute:

```bash
git clone https://github.com/Maitrisoni1803/Intelligent-Warehouse-Robot-Task-Selection-and-Path-Planning.git
```

### Step 2: Open the Project Folder

```bash
cd Intelligent-Warehouse-Robot-Task-Selection-and-Path-Planning
```

Open the folder in Visual Studio Code.

### Step 3: Check Python Installation

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

## ▶️ 9. How to Run the Project

### A. Run the Complete Simulation

Execute the following command in the VS Code terminal:

```bash
python main.py
```

Or on Windows:

```bash
py main.py
```

This runs the complete warehouse robot simulation.

### B. Run the Graphical User Interface

To see the robot moving visually inside the warehouse, execute:

```bash
python gui.py
```

**GUI Controls:**

| Button | Function |
|---|---|
| **Start Simulation** | Starts automatic robot movement. |
| **Pause** | Pauses the simulation. |
| **Next Step** | Moves the robot to the next step. |
| **Reset** | Restarts the simulation. |

### C. Run Heuristic Comparison

To compare the four heuristic functions, execute:

```bash
python compare_heuristics.py
```

The program generates comparison results, which can be viewed in:

```text
heuristic_comparison.csv
```

### D. Run Using Jupyter Notebook

Open the notebook:

```text
compare_heuristics (1).ipynb
```

Select the Python kernel and click **Run All** to execute the notebook cells.

**Note:** The graphical interface runs in a separate desktop window, not directly inside the notebook output.

## 📊 10. Performance Evaluation

The project evaluates the A* algorithm using the following performance parameters:

| Parameter | Meaning |
|---|---|
| **Path Cost** | Total cost of the path found by the algorithm. |
| **Expanded Nodes** | Number of nodes explored during pathfinding. |
| **Execution Time** | Time taken by the algorithm to find a path. |

The heuristic comparison program generates the results for all four heuristic functions.

These measurements help evaluate the efficiency of different heuristic approaches.

## 🗺️ 11. Warehouse Map Representation

The warehouse environment is represented using a grid.

| Symbol | Meaning |
|---|---|
| `#` | Blocked cell / Shelf / Wall |
| `.` | Open floor |
| `S` | Robot starting position |
| `P` | Packing station |

**Coordinate System:**

- Coordinates are represented as `(row, column)`.
- The top-left corner starts at `(0, 0)`.
- The robot moves in four directions: Up, Down, Left, and Right.

**Important:** If you modify the warehouse map, update the corresponding task coordinates in `tasks.py`.

## ⚠️ 12. Project Limitations

- This project is a simulated warehouse environment, not a physical robot.
- The warehouse obstacles are static in the supplied demonstration.
- Robot movement is limited to four directions.
- Task deadlines are used as an urgency input and do not represent a real-time deadline guarantee.
- The heuristic comparison uses a fixed route sequence to support a fair comparison of pathfinding methods.

## 🚀 13. Future Enhancements

The project can be extended with the following improvements:

- Multiple robots working together in the same warehouse.
- Dynamic obstacle detection and avoidance.
- Real-time task allocation and scheduling.
- Advanced battery optimization.
- Integration with real robotic hardware.
- Machine learning-based task prioritization.
- Live warehouse monitoring and analytics dashboard.

## 👩‍💻 14. Author

**Maitri Soni**

GitHub: [@Maitrisoni1803](https://github.com/Maitrisoni1803)

**Project:** Intelligent Warehouse Robot – Task Selection and Path Planning

## ⭐ 15. Conclusion

The Intelligent Warehouse Robot project demonstrates how Artificial Intelligence and search algorithms can be applied to warehouse automation.

By combining intelligent task selection, A* path planning, heuristic comparison, obstacle avoidance, and battery management, the project provides a practical example of autonomous robot decision-making.

The simulation helps understand how AI techniques can improve warehouse navigation and task execution.

---

<p align="center">
  <strong>🤖 Intelligent Warehouse Robot | AI-Based Path Planning | Python</strong>
  <br>
  <em>Thank you for visiting this repository!</em>
</p>