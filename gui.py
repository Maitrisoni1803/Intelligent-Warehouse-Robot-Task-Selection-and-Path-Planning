
"""Full-screen Warehouse Robot AI Dashboard.
Run: python gui.py
"""

import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from warehouse import Warehouse
from astar import astar
from agent import WarehouseAgent
from tasks import (
    TASKS,
    CHARGER,
    BATTERY_CAPACITY,
    ENERGY_PER_STEP,
    BATTERY_RESERVE
)

ROOT = Path(__file__).resolve().parent

# Colour theme
BG = "#EEF2F7"
BLUE = "#3478F6"
BLUE_LIGHT = "#DCE9FF"
GREEN = "#16A36A"
GREEN_LIGHT = "#DDF5E9"
ORANGE = "#F39B38"
ORANGE_LIGHT = "#FFF0D9"
RED = "#E65353"
TEXT = "#243247"
MUTED = "#718096"
WHITE = "#FFFFFF"
WALL = "#455468"
FLOOR = "#F1F5F9"


class WarehouseGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Warehouse AI | Intelligent Robot Simulation")
        self.root.geometry("1450x900")
        self.root.minsize(1100, 720)
        self.root.configure(bg=BG)

        self.w = Warehouse(ROOT / "map.txt")
        self.cell = 42

        self.task_pos = {
            task["position"]: task for task in TASKS
        }

        self.events = []
        self.index = 0
        self.running = False
        self.after_id = None
        self.finished = False

        self.reset_data()
        self.build_ui()
        self.update_status()
        self.draw()

    # ---------------- DATA ----------------

    def reset_data(self):
        self.robot = self.w.start
        self.battery = BATTERY_CAPACITY
        self.distance = 0
        self.expanded = 0

        self.collected = set()
        self.delivered = set()
        self.path_seen = set()

        self.current = "Waiting to start"
        self.message = "Ready. Start the simulation."

        self.events = []
        self.index = 0
        self.finished = False

    # ---------------- UI ----------------

    def build_ui(self):

        self.content = tk.Frame(self.root, bg=BG)
        self.content.pack(
            fill="both", expand=True,
            padx=25, pady=20
        )

        # Header
        header = tk.Frame(self.content, bg=BG)
        header.pack(fill="x", pady=(0, 18))

        title_area = tk.Frame(header, bg=BG)
        title_area.pack(side="left")

        tk.Label(
            title_area,
            text="Warehouse AI Dashboard",
            font=("Segoe UI", 24, "bold"),
            bg=BG, fg=TEXT
        ).pack(anchor="w")

        tk.Label(
            title_area,
            text="Intelligent task selection | A* path planning | Battery management",
            font=("Segoe UI", 10),
            bg=BG, fg=MUTED
        ).pack(anchor="w", pady=4)

        self.status_badge = tk.Label(
            header,
            text="● READY",
            bg=GREEN_LIGHT,
            fg=GREEN,
            font=("Segoe UI", 10, "bold"),
            padx=16, pady=10
        )
        self.status_badge.pack(side="right", pady=8)

        # Metric cards
        metrics = tk.Frame(self.content, bg=BG)
        metrics.pack(fill="x", pady=(0, 17))

        self.metric_labels = {}

        cards = [
            ("tasks", "TASKS DELIVERED", "0 / 4", BLUE, "▣"),
            ("battery", "BATTERY LEVEL", "100%", GREEN, "ϟ"),
            ("distance", "DISTANCE TRAVELLED", "0 moves", ORANGE, "↗"),
            ("nodes", "A* NODES EXPANDED", "0", "#8B65D8", "⌘")
        ]

        for key, heading, value, colour, symbol in cards:

            card = tk.Frame(
                metrics,
                bg=WHITE,
                highlightbackground="#DFE6EF",
                highlightthickness=1
            )

            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=(0, 12)
            )

            top = tk.Frame(card, bg=WHITE)
            top.pack(fill="x", padx=14, pady=(13, 5))

            tk.Label(
                top,
                text=symbol,
                bg=colour,
                fg=WHITE,
                font=("Segoe UI", 15, "bold"),
                width=2
            ).pack(side="left")

            tk.Label(
                top,
                text=heading,
                bg=WHITE,
                fg=MUTED,
                font=("Segoe UI", 8, "bold")
            ).pack(side="left", padx=9)

            value_label = tk.Label(
                card,
                text=value,
                bg=WHITE,
                fg=TEXT,
                font=("Segoe UI", 23, "bold")
            )

            value_label.pack(
                anchor="w",
                padx=15,
                pady=(2, 13)
            )

            self.metric_labels[key] = value_label

        # Main workspace
        workspace = tk.Frame(self.content, bg=BG)
        workspace.pack(fill="both", expand=True)

        # Warehouse map card
        map_card = tk.Frame(
            workspace,
            bg=WHITE,
            highlightbackground="#DFE6EF",
            highlightthickness=1
        )

        map_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 14)
        )

        map_header = tk.Frame(map_card, bg=WHITE)
        map_header.pack(fill="x", padx=17, pady=14)

        tk.Label(
            map_header,
            text="Warehouse Simulation",
            font=("Segoe UI", 14, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(side="left")

        tk.Label(
            map_header,
            text="LIVE MAP",
            bg=BLUE_LIGHT,
            fg=BLUE,
            font=("Segoe UI", 8, "bold"),
            padx=9,
            pady=5
        ).pack(side="right")

        self.canvas = tk.Canvas(
            map_card,
            bg="#E8EEF6",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        self.canvas.bind(
            "<Configure>",
            lambda event: self.draw()
        )

        # Right information panel
        right = tk.Frame(workspace, bg=BG, width=300)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        # Robot status
        status_card = self.make_card(right)

        tk.Label(
            status_card,
            text="ROBOT STATUS",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", padx=15, pady=(14, 10))

        self.current_label = tk.Label(
            status_card,
            text="Waiting to start",
            bg=WHITE,
            fg=BLUE,
            font=("Segoe UI", 12, "bold")
        )
        self.current_label.pack(anchor="w", padx=15)

        self.position_label = tk.Label(
            status_card,
            text="Position: (1, 1)",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 9)
        )
        self.position_label.pack(
            anchor="w",
            padx=15,
            pady=(5, 15)
        )

        # Battery card
        battery_card = self.make_card(right)

        tk.Label(
            battery_card,
            text="ENERGY MANAGEMENT",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", padx=15, pady=(13, 8))

        self.battery_text = tk.Label(
            battery_card,
            text="100%",
            bg=WHITE,
            fg=GREEN,
            font=("Segoe UI", 20, "bold")
        )
        self.battery_text.pack(anchor="w", padx=15)

        self.battery_canvas = tk.Canvas(
            battery_card,
            height=14,
            bg="#E5EAF0",
            highlightthickness=0
        )

        self.battery_canvas.pack(
            fill="x",
            padx=15,
            pady=10
        )

        self.battery_bar = self.battery_canvas.create_rectangle(
            0, 0, 200, 14,
            fill=GREEN,
            outline=""
        )

        self.charge_label = tk.Label(
            battery_card,
            text="● Normal power",
            bg=WHITE,
            fg=GREEN,
            font=("Segoe UI", 9)
        )

        self.charge_label.pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

        # Task progress card
        task_card = self.make_card(right)

        tk.Label(
            task_card,
            text="TASK PROGRESS",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", padx=15, pady=(13, 9))

        self.task_rows = {}

        for task in TASKS:

            row = tk.Frame(task_card, bg=WHITE)
            row.pack(fill="x", padx=15, pady=4)

            tk.Label(
                row,
                text=task["id"],
                bg=BLUE_LIGHT,
                fg=BLUE,
                font=("Segoe UI", 9, "bold"),
                width=4,
                pady=4
            ).pack(side="left")

            tk.Label(
                row,
                text="Priority " + str(task["priority"]),
                bg=WHITE,
                fg=MUTED,
                font=("Segoe UI", 9)
            ).pack(side="left", padx=8)

            status = tk.Label(
                row,
                text="Pending",
                bg="#F0F2F5",
                fg=MUTED,
                font=("Segoe UI", 8, "bold"),
                padx=6,
                pady=4
            )

            status.pack(side="right")
            self.task_rows[task["id"]] = status

        tk.Frame(
            task_card,
            bg=WHITE,
            height=12
        ).pack()

        # Activity log
        activity_card = self.make_card(right, expand=True)

        tk.Label(
            activity_card,
            text="LIVE ACTIVITY",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", padx=14, pady=(12, 7))

        self.activity = tk.Listbox(
            activity_card,
            bg="#F7F9FC",
            fg=TEXT,
            font=("Segoe UI", 9),
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            selectbackground=BLUE_LIGHT
        )

        self.activity.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # Bottom controls
        controls = tk.Frame(
            self.content,
            bg=WHITE,
            highlightbackground="#DFE6EF",
            highlightthickness=1
        )

        controls.pack(fill="x", pady=(15, 0))

        tk.Label(
            controls,
            text="SIMULATION CONTROLS",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 8, "bold")
        ).pack(side="left", padx=15)

        self.start_btn = self.make_button(
            controls, "▶ START",
            GREEN, WHITE, self.start
        )

        self.pause_btn = self.make_button(
            controls, "Ⅱ PAUSE",
            ORANGE, WHITE, self.pause
        )

        self.step_btn = self.make_button(
            controls, "→ STEP",
            BLUE, WHITE, self.step
        )

        self.reset_btn = self.make_button(
            controls, "↻ RESET",
            "#E9EEF5", TEXT, self.reset
        )

        self.start_btn.pack(side="right", padx=7, pady=11)
        self.pause_btn.pack(side="right", padx=7, pady=11)
        self.step_btn.pack(side="right", padx=7, pady=11)
        self.reset_btn.pack(side="right", padx=7, pady=11)

        self.pause_btn.config(state="disabled")
        self.step_btn.config(state="disabled")

    def make_card(self, parent, expand=False):
        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#DFE6EF",
            highlightthickness=1
        )

        card.pack(
            fill="both" if expand else "x",
            expand=expand,
            pady=(0, 13)
        )

        return card

    def make_button(self, parent, text, bg, fg, command):
        return tk.Button(
            parent,
            text=text,
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            relief="flat",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            padx=15,
            pady=9,
            cursor="hand2",
            command=command
        )

    # ---------------- AI SIMULATION ----------------

    def build_events(self):
        self.events = []
        pos = self.w.start
        battery = BATTERY_CAPACITY
        done = set()

        chooser = WarehouseAgent(self.w, "manhattan")

        def add_moves(path, label):
            nonlocal pos, battery

            for point in path[1:]:
                self.events.append(("move", point, label))
                pos = point
                battery -= ENERGY_PER_STEP

        def route(goal, label):
            nonlocal pos, battery

            path, nodes = astar(
                self.w, pos, goal, "manhattan"
            )
            self.expanded += nodes

            if not path:
                raise RuntimeError("No path found to " + label)

            required = (len(path) - 1) * ENERGY_PER_STEP

            if goal != CHARGER and (
                battery <= 40 or
                battery < required + BATTERY_RESERVE
            ):

                charge_path, charge_nodes = astar(
                    self.w, pos, CHARGER, "manhattan"
                )
                self.expanded += charge_nodes

                if not charge_path:
                    raise RuntimeError(
                        "No path to charging station"
                    )

                charge_required = (
                    (len(charge_path) - 1) * ENERGY_PER_STEP
                )

                if battery < charge_required:
                    raise RuntimeError(
                        "Battery too low to reach charging station. "
                        "Move the charging station closer."
                    )

                self.events.append((
                    "msg",
                    "Battery low. Going to charging station."
                ))

                add_moves(charge_path, "charging station")

                self.events.append((
                    "charge",
                    BATTERY_CAPACITY,
                    "Battery recharged to 100%."
                ))

                battery = BATTERY_CAPACITY
                pos = CHARGER

                path, nodes = astar(
                    self.w, pos, goal, "manhattan"
                )
                self.expanded += nodes

                if not path:
                    raise RuntimeError(
                        "No path found after charging to " + label
                    )

            add_moves(path, label)

            self.events.append((
                "msg",
                "Reached " + label + "."
            ))

        while len(done) < len(TASKS):

            chooser.position = pos
            chooser.collected = set(done)

            task = chooser.select_task()

            if task is None:
                break

            self.events.append((
                "select",
                task["id"],
                "Selected " + task["id"] +
                " (priority " + str(task["priority"]) + ")."
            ))

            route(task["position"], task["id"])

            done.add(task["id"])

            self.events.append((
                "collect",
                task["id"],
                task["id"] + " collected."
            ))

            route(self.w.packing, "packing station")

            self.events.append((
                "deliver",
                task["id"],
                task["id"] + " delivered."
            ))

        route(self.w.start, "home/start")

        self.events.append((
            "finish",
            "All tasks delivered. Robot returned to start."
        ))

    # ---------------- CONTROLS ----------------

    def start(self):
        if self.finished:
            return

        if not self.events:
            try:
                self.build_events()
            except Exception as error:
                messagebox.showerror(
                    "Simulation error",
                    str(error)
                )
                return

        self.running = True

        self.status_badge.config(
            text="● RUNNING",
            bg=GREEN_LIGHT,
            fg=GREEN
        )

        self.start_btn.config(state="disabled")
        self.pause_btn.config(state="normal")
        self.step_btn.config(state="disabled")

        self.animate()

    def pause(self):
        self.running = False

        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        if not self.finished:
            self.status_badge.config(
                text="● PAUSED",
                bg=ORANGE_LIGHT,
                fg="#B36A12"
            )

            self.pause_btn.config(state="disabled")
            self.step_btn.config(state="normal")

    def step(self):
        if self.finished:
            return

        if not self.events:
            try:
                self.build_events()
            except Exception as error:
                messagebox.showerror(
                    "Simulation error",
                    str(error)
                )
                return

        self.process_event()
        self.update_status()
        self.draw()

    def animate(self):
        if not self.running:
            return

        self.process_event()
        self.update_status()
        self.draw()

        if self.finished:
            self.running = False

            self.status_badge.config(
                text="● COMPLETED",
                bg=GREEN_LIGHT,
                fg=GREEN
            )

            self.start_btn.config(state="disabled")
            self.pause_btn.config(state="disabled")
            self.step_btn.config(state="disabled")

            messagebox.showinfo(
                "Simulation completed",
                "All warehouse tasks have been delivered!\n\n"
                "Distance: " + str(self.distance) +
                " moves\nBattery: " + str(self.battery) + "%\n"
                "Tasks: " + str(len(self.delivered)) +
                "/" + str(len(TASKS))
            )
            return

        self.after_id = self.root.after(
            250,
            self.animate
        )

    def process_event(self):
        if self.index >= len(self.events):
            self.finished = True
            return

        event = self.events[self.index]
        self.index += 1

        kind = event[0]

        if kind == "move":
            self.robot = event[1]
            self.distance += 1
            self.battery -= ENERGY_PER_STEP
            self.path_seen.add(self.robot)
            self.message = "Moving towards " + event[2]

        elif kind == "select":
            self.current = event[1]
            self.message = event[2]

        elif kind == "collect":
            self.collected.add(event[1])
            self.message = event[2]

        elif kind == "deliver":
            self.delivered.add(event[1])
            self.message = event[2]

        elif kind == "charge":
            self.battery = event[1]
            self.message = event[2]

        elif kind == "msg":
            self.message = event[1]

        elif kind == "finish":
            self.message = event[1]
            self.current = "Completed"
            self.finished = True

        self.add_activity(self.message)

    def add_activity(self, message):
        self.activity.insert("end", "•  " + message)
        self.activity.see("end")

    def reset(self):
        self.pause()
        self.reset_data()
        self.activity.delete(0, "end")

        self.status_badge.config(
            text="● READY",
            bg=GREEN_LIGHT,
            fg=GREEN
        )

        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled")
        self.step_btn.config(state="disabled")

        self.add_activity("Simulation reset.")
        self.update_status()
        self.draw()

    # ---------------- STATUS ----------------

    def update_status(self):

        self.metric_labels["tasks"].config(
            text=str(len(self.delivered)) +
            " / " + str(len(TASKS))
        )

        self.metric_labels["battery"].config(
            text=str(self.battery) + "%"
        )

        self.metric_labels["distance"].config(
            text=str(self.distance) + " moves"
        )

        self.metric_labels["nodes"].config(
            text=str(self.expanded)
        )

        self.current_label.config(text=self.current)

        self.position_label.config(
            text="Robot position: " + str(self.robot)
        )

        self.battery_text.config(
            text=str(self.battery) + "%"
        )

        width = self.battery_canvas.winfo_width()

        if width < 10:
            width = 220

        bar_width = width * max(
            0,
            min(1, self.battery / BATTERY_CAPACITY)
        )

        colour = (
            GREEN if self.battery > 30
            else ORANGE if self.battery > 15
            else RED
        )

        self.battery_canvas.coords(
            self.battery_bar,
            0, 0, bar_width, 14
        )

        self.battery_canvas.itemconfig(
            self.battery_bar,
            fill=colour
        )

        if "recharged" in self.message.lower():
            self.charge_label.config(
                text="⚡ Battery recharged",
                fg=GREEN
            )

        elif self.battery <= 15:
            self.charge_label.config(
                text="● Low battery",
                fg=RED
            )

        else:
            self.charge_label.config(
                text="● Normal power",
                fg=GREEN
            )

        for task in TASKS:

            task_id = task["id"]
            label = self.task_rows[task_id]

            if task_id in self.delivered:
                label.config(
                    text="Delivered",
                    bg=GREEN_LIGHT,
                    fg=GREEN
                )

            elif task_id in self.collected:
                label.config(
                    text="Collected",
                    bg=BLUE_LIGHT,
                    fg=BLUE
                )

            elif task_id == self.current:
                label.config(
                    text="In progress",
                    bg=ORANGE_LIGHT,
                    fg="#B36A12"
                )

            else:
                label.config(
                    text="Pending",
                    bg="#F0F2F5",
                    fg=MUTED
                )

    # ---------------- WAREHOUSE MAP ----------------

    def draw(self):
        if not hasattr(self, "canvas"):
            return

        self.canvas.delete("all")

        available_w = max(
            300,
            self.canvas.winfo_width() - 20
        )

        available_h = max(
            300,
            self.canvas.winfo_height() - 20
        )

        cell = min(
            self.cell,
            available_w // self.w.cols,
            available_h // self.w.rows
        )

        cell = max(20, cell)

        total_w = self.w.cols * cell
        total_h = self.w.rows * cell

        left = (
            self.canvas.winfo_width() - total_w
        ) / 2

        top = (
            self.canvas.winfo_height() - total_h
        ) / 2

        for r in range(self.w.rows):
            for c in range(self.w.cols):

                pos = (r, c)
                symbol = self.w.grid[r][c]

                x = left + c * cell
                y = top + r * cell

                fill = WALL if symbol == "#" else FLOOR

                if pos in self.path_seen and symbol == ".":
                    fill = BLUE_LIGHT

                if symbol == "P":
                    fill = BLUE

                if pos == CHARGER:
                    fill = ORANGE_LIGHT

                if (
                    pos in self.task_pos
                    and self.task_pos[pos]["id"] not in self.delivered
                ):
                    fill = GREEN_LIGHT

                self.canvas.create_rectangle(
                    x, y,
                    x + cell - 2,
                    y + cell - 2,
                    fill=fill,
                    outline="#D5DEE9",
                    width=1
                )

                label = ""
                label_colour = TEXT

                if symbol == "P":
                    label = "PACK"
                    label_colour = WHITE

                elif pos == CHARGER:
                    label = "CHG"
                    label_colour = "#A45A08"

                elif pos in self.task_pos:
                    task_id = self.task_pos[pos]["id"]

                    label = (
                        "✓" if task_id in self.delivered
                        else task_id
                    )

                    label_colour = GREEN

                elif pos == self.w.start:
                    label = "START"
                    label_colour = MUTED

                if label:
                    self.canvas.create_text(
                        x + cell / 2,
                        y + cell / 2,
                        text=label,
                        fill=label_colour,
                        font=(
                            "Segoe UI",
                            max(7, cell // 5),
                            "bold"
                        )
                    )

        # Draw robot last
        r, c = self.robot

        cx = left + c * cell + cell / 2
        cy = top + r * cell + cell / 2

        radius = cell * 0.34

        self.canvas.create_oval(
            cx - radius,
            cy - radius,
            cx + radius,
            cy + radius,
            fill=RED,
            outline=WHITE,
            width=2
        )

        self.canvas.create_text(
            cx, cy,
            text="R",
            fill=WHITE,
            font=(
                "Segoe UI",
                max(9, cell // 4),
                "bold"
            )
        )


def main():
    root = tk.Tk()
    WarehouseGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
