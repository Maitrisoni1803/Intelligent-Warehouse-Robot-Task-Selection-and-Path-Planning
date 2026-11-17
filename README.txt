INTELLIGENT WAREHOUSE ROBOT AI PROJECT
======================================

TITLE
Intelligent Warehouse Robot Task Selection and Path Planning Using Heuristic Search

REQUIREMENTS
- Python 3.9 or newer recommended
- Visual Studio Code
- Python extension for VS Code
- No pip packages are required

FILES
main.py                 Runs the complete robot simulation
warehouse.py            Loads and represents the grid warehouse
tasks.py                Stores task, charger and battery settings
agent.py                Reflex rules and task-selection logic
astar.py                A* search and four heuristics
compare_heuristics.py   Runs the four-heuristic comparison
map.txt                 Warehouse grid
heuristic_comparison.csv Generated comparison results
report_template.md      Two-page report starting point

RUN IN VS CODE (WINDOWS)
1. Extract the ZIP file to a normal folder, e.g. Desktop\Warehouse_Robot_AI_Project.
2. Open VS Code.
3. Select File > Open Folder and choose that extracted folder.
4. Open Terminal > New Terminal.
5. Check Python:
      py --version
   If that does not work, try:
      python --version
6. Run the simulation:
      py main.py
   or:
      python main.py
7. Run the A* comparison:
      py compare_heuristics.py
   or:
      python compare_heuristics.py
8. Open heuristic_comparison.csv to see the generated results.

HOW TO CHANGE THE MAP
- # means blocked shelf/wall
- . means open floor
- S means robot start
- P means packing station
- Keep every row the same length.
- If you change the map, update task coordinates in tasks.py too.
- Coordinates are (row, column), starting from zero at the top-left.

IMPORTANT
This is a single-robot grid simulation. Movement is in four directions.
Each move costs one battery unit. The robot recharges at the charger coordinate
when its battery is not sufficient for the planned trip plus reserve.
The task score is a simple explainable rule using priority, deadline urgency
and distance. The exact weights are configurable in agent.py.

PROJECT DEMONSTRATION
1. Run main.py and explain the map.
2. Explain how the agent scores and selects a task.
3. Explain how A* finds a path.
4. Explain the four heuristics.
5. Run compare_heuristics.py and open the CSV.
6. Explain path cost, expanded nodes and execution time.

LIMITATIONS
- The environment is a simulated grid, not a physical robot.
- Obstacles are static in the supplied demonstration.
- The deadline value is used as an urgency input; this version does not
  simulate a real clock or guarantee deadline completion.
- The four heuristic comparison uses the same fixed route sequence so that
  the pathfinding methods can be compared fairly.


GUI SIMULATION
1. Open PowerShell in this project folder.
2. Run: python gui.py
3. Click Start Simulation to watch the robot move automatically.
4. Use Pause, Next Step and Reset to control the simulation.

The GUI uses the existing map, task definitions, task-selection logic and A*
search. It uses built-in Tkinter; no pip installation is normally required.
