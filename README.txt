# 🤖 Intelligent Warehouse Robot
### AI-Based Task Selection and Path Planning Using A* Search

<p align="center">
  <b>A Python-based warehouse simulation using Artificial Intelligence, heuristic search, and intelligent task selection.</b>
</p>

---

## 📌 Project Overview

The **Intelligent Warehouse Robot** is an AI-based simulation designed to demonstrate how an autonomous robot can perform tasks inside a warehouse environment.

In a warehouse, robots need to identify tasks, select which task to perform, find the shortest possible path, avoid obstacles, and manage their battery efficiently.

This project implements an intelligent warehouse robot using **A* (A-Star) Search**, heuristic functions, task-priority selection, and battery-aware navigation.

The robot operates in a grid-based warehouse containing obstacles, task locations, a packing station, and a charging station. It automatically selects tasks, plans routes, moves through the warehouse, and returns for charging when required.

The project also includes a graphical user interface (GUI) to visualize the robot's movement and a heuristic comparison module to evaluate different pathfinding strategies.

## 🎯 Project Objectives

- Develop an intelligent robot for a grid-based warehouse environment.
- Implement A* search for efficient path planning.
- Select tasks based on priority, deadline urgency, and distance.
- Avoid obstacles while navigating through the warehouse.
- Monitor battery consumption and manage recharging.
- Compare different heuristic functions used in A* search.
- Visualize robot movement through a graphical interface.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 Intelligent Task Selection | Selects tasks using priority, urgency, and distance. |
| 🗺️ A* Path Planning | Finds a path through the warehouse grid. |
| 🚧 Obstacle Avoidance | Prevents movement through blocked cells. |
| 🔋 Battery Management | Tracks battery usage and charging requirements. |
| 📦 Packing Station | Provides a destination for completed warehouse tasks. |
| 🔌 Charging Station | Allows the robot to recharge its battery. |
| 📊 Heuristic Comparison | Compares four heuristic functions. |
| 🖥️ Graphical Interface | Displays and controls the robot simulation. |

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Artificial Intelligence:** A* Search Algorithm
- **Pathfinding:** Heuristic Search
- **Visualization:** Tkinter
- **Data Handling:** CSV
- **Development Environment:** Visual Studio Code and Jupyter Notebook

## 🧠 Algorithms and Methodology

### 1. A* Search Algorithm

A* is an informed search algorithm used to find an efficient path between a starting point and a destination.

It evaluates each node using:

**f(n) = g(n) + h(n)**

Where:

- `g(n)` = Actual cost from the starting point to the current node.
- `h(n)` = Estimated cost from the current node to the destination.
- `f(n)` = Total estimated cost of the path.

The algorithm selects the node with the lowest estimated total cost and continues until it reaches the destination.

### 2. Heuristic Functions

This project compares four heuristic approaches:

| Heuristic | Description |
|---|---|
| Manhattan Distance | Calculates distance using horizontal and vertical movement. |
| Euclidean Distance | Calculates straight-line distance between two points. |
| Chebyshev Distance | Uses the maximum difference between horizontal and vertical coordinates. |
| Zero Heuristic | Uses zero as the estimated remaining cost, behaving like Uniform Cost Search. |

The comparison helps understand how heuristic selection affects search efficiency.

### 3. Intelligent Task Selection

The robot selects tasks using a simple scoring strategy based on:

- Task priority
- Deadline urgency
- Distance from the robot

The task-selection logic is implemented in `agent.py`.

### 4. Battery Management

The robot starts with a limited battery capacity.

- Each movement step consumes one battery unit.
- The robot checks whether its battery is sufficient for the planned journey and reserve.
- It uses the charging station when additional battery power is required.

This helps demonstrate battery-aware navigation.

## 🏗️ Project Architecture

The project is organized into separate Python modules, with each file responsible for a specific part of the simulation.

| File | Purpose |
|---|---|
| `main.py` | Runs the complete warehouse robot simulation. |
| `gui.py` | Provides the graphical interface for the simulation. |
| `warehouse.py` | Loads and represents the warehouse grid. |
| `agent.py` | Handles robot behavior and intelligent task selection. |
| `astar.py` | Implements A* search and heuristic functions. |
| `tasks.py` | Stores task, charging, and battery configurations. |
| `compare_heuristics.py` | Compares the performance of four heuristics. |
| `map.txt` | Contains the warehouse grid layout. |
| `heuristic_comparison.csv` | Stores heuristic comparison results. |
| `compare_heuristics (1).ipynb` | Jupyter Notebook for exploring heuristic comparison. |

## 📂 Repository Structure

```text
Intelligent-Warehouse-Robot/
│
├── agent.py
├── astar.py
├── compare_heuristics.py
├── compare_heuristics (1).ipynb
├── gui.py
├── main.py
├── tasks.py
├── warehouse.py
├── map.txt
├── heuristic_comparison.csv
│
├── README.md
└── Warehouse_Robot_AI_Course Project.zip
```

## ⚙️ Installation and Setup

### Prerequisites

Before running the project, make sure you have:

- Python 3.9 or above
- Visual Studio Code
- Python extension for VS Code

**Note:** The project uses Python's built-in Tkinter library for the GUI. No additional pip packages are normally required for the supplied simulation.

### Step 1: Clone the Repository

Open your terminal and execute:

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

If you are using Windows and the above command does not work, try:

```bash
py --version
```

## ▶️ How to Run the Project

### 1. Run the Complete Simulation

Execute the following command in the VS Code terminal:

```bash
python main.py
```

This runs the complete warehouse robot simulation in the terminal.

### 2. Run the Graphical User Interface

To visualize the robot's movement, execute:

```bash
python gui.py
```

The GUI provides controls to interact with the simulation:

- **Start Simulation:** Starts automatic robot movement.
- **Pause:** Pauses the simulation.
- **Next Step:** Moves the simulation forward one step.
- **Reset:** Resets the simulation.

### 3. Run the Heuristic Comparison

Execute:

```bash
python compare_heuristics.py
```

This runs the comparison of Manhattan, Euclidean, Chebyshev, and Zero heuristics.

The results are saved in:

```text
heuristic_comparison.csv
```

## 📓 Running the Jupyter Notebook

The project also includes a Jupyter Notebook for exploring the heuristic comparison.

1. Open the project folder in VS Code.
2. Open the `.ipynb` notebook file.
3. Select the Python kernel.
4. Click **Run All**.
5. Review the outputs and comparison results.

To execute the Python simulation from a notebook cell, you can also use:

```python
%run main.py
```

To run the heuristic comparison:

```python
%run compare_heuristics.py
```

For the graphical interface, run `gui.py` from the VS Code terminal because it opens a separate desktop window.

## 📊 Performance Evaluation

The project evaluates the performance of different heuristic functions using:

- **Path Cost:** Total movement cost of the selected path.
- **Expanded Nodes:** Number of nodes explored during the search.
- **Execution Time:** Time taken by the search algorithm.

The comparison uses a fixed route sequence to evaluate the heuristic approaches under the same conditions.

The CSV file contains the generated comparison results and can be opened using Excel, VS Code, or Python.

## 🗺️ Warehouse Environment

The warehouse is represented as a two-dimensional grid.

| Symbol | Meaning |
|---|---|
| `#` | Obstacle or blocked shelf |
| `.` | Free movement area |
| `S` | Robot starting position |
| `P` | Packing station |

The robot moves in four directions: up, down, left, and right.

Coordinates are represented as `(row, column)`, starting from zero at the top-left corner.

## 🔍 Expected Project Workflow

```text
        Start Simulation
                |
                v
       Load Warehouse Map
                |
                v
       Initialize Robot
                |
                v
        Identify Tasks
                |
                v
      Select Best Task
                |
                v
       Plan Path Using A*
                |
                v
      Check Battery Level
                |
          +-----+-----+
          |           |
       Enough       Not Enough
          |           |
          |           v
          |      Visit Charging
          |         Station
          |           |
          +-----<-----+
                |
                v
       Navigate to Task
                |
                v
       Complete Task
                |
                v
       Continue Until
        Tasks Complete
                |
                v
             End
```

## ⚠️ Project Limitations

- This is a simulated warehouse environment, not a physical robot.
- The supplied warehouse obstacles are static.
- The robot operates as a single-agent system.
- Deadline values are used as urgency inputs; real-time deadline completion is not guaranteed.
- The heuristic comparison uses a fixed route sequence for a fair comparison.

## 🚀 Future Enhancements

The project can be extended with:

- Multiple autonomous warehouse robots.
- Dynamic obstacle detection and avoidance.
- Real-time task scheduling.
- Improved battery optimization.
- Machine learning-based task prioritization.
- Real-world robot integration.
- Advanced warehouse visualization.

## 🎓 Learning Outcomes

Through this project, we explored:

- Artificial Intelligence and informed search.
- A* pathfinding and heuristic functions.
- Task selection and decision-making.
- Grid-based environment modeling.
- Battery-aware robot navigation.
- Algorithm performance evaluation.
- Python GUI development and simulation.

