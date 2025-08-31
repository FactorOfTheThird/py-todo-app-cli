from enum import Enum
import json


class Color(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


class App:

    def __init__(self, tasks: dict[int, dict[str, str]]):
        self.commands = {
            "h": self.help,
            "q": self.quit,

            "add": self.addTask,
            "list": self.listTasks,
            "rem": self.removeTask,

            "save": self.saveTasks,
            "load": self.importTasks
        }

        self.tasks = tasks

    def help(self):
        """Displays all possible commands and their role."""
        for cmd, method in self.commands.items():
            doc = method.__doc__ or "No description available."
            print(f"{Color.YELLOW.value}\t{cmd} > {doc}{Color.RESET.value}")

    def quit(self):
        """Quits the program"""
        exit()

    def getCommand(self, cmd: str):
        return self.commands.get(cmd)

    def addTask(self):
        """Adds a new task with a title and description."""

        title = input(f"{Color.YELLOW.value}\tNew task title > {Color.RESET.value}").strip()
        description = input(f"{Color.YELLOW.value}\tNew task description > {Color.RESET.value}").strip()

        if len(title) == 0 or len(description) == 0:
            print(f"\t{Color.RED.value}Title and description cannot be empty!{Color.RESET.value}")
            return

        try:
            next_id = max(self.tasks.keys()) + 1
        except ValueError:
            next_id = 1

        self.tasks[next_id] = {
            "title": title,
            "description": description
        }
        print(f"{Color.GREEN.value}Task added successfuly.{Color.RESET.value}")

    def listTasks(self):
        """Lists all tasks in the database."""

        if len(self.tasks) == 0:
            print(f"{Color.RED.value}No tasks to show, add some with the 'add' command.{Color.RESET.value}")
            return

        print(f"{Color.YELLOW.value}You have {len(self.tasks)} {'task' if len(self.tasks) == 1 else 'tasks'}:\n{Color.RESET.value}")

        for id, taskData in self.tasks.items():
            title = taskData["title"]
            description = taskData["description"]
            print(10 * "-")
            print(f"{Color.BLUE.value}Task {id}{Color.RESET.value}\n\t{Color.BLUE.value}Title:{Color.RESET.value} {title}\n\t{Color.BLUE.value}Description:{Color.RESET.value} {description}")
            print(10 * "-")

        print(f"\n{Color.YELLOW.value}No more tasks to show.{Color.RESET.value}")

    def removeTask(self):
        """Removes a task with given ID"""

        try:
            taskID = int(input(f"\t{Color.YELLOW.value}Task ID to delete > {Color.RESET.value}").strip())
            taskID = int(taskID)
            del self.tasks[taskID]

            print(f"\t{Color.GREEN.value}Removed successfuly!{Color.RESET.value}")
        except KeyError:
            print(f"\t{Color.RED.value}No task with ID {taskID} found.{Color.RESET.value}")
        except ValueError:
            print(f"\t{Color.RED.value}Task ID must be a number, not a string.{Color.RESET.value}")

    def saveTasks(self):
        """Saves all tasks to a JSON file."""
        filename = input(f"\t{Color.YELLOW.value}Full file name > {Color.RESET.value}").strip()

        with open(filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

        print(f"\t{Color.GREEN.value}Tasks saved to file '{filename}'!{Color.RESET.value}")

    def loadTasks(self, filename="tasks.json"):
        """Loads tasks from a JSON file."""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def importTasks(self):
        """Imports and loads tasks from an external JSON file."""
        filename = input(f"\t{Color.YELLOW.value}Full file name to import from > {Color.RESET.value}").strip()

        imported = self.loadTasks(filename)
        for taskIDStr, taskData in imported.items():
            taskID = int(taskIDStr)
            self.tasks[taskID] = taskData

        print(f"\t{Color.GREEN.value}Tasks imported successfuly!{Color.RESET.value}")


app = App({})

while True:
    userInput = input("Command (h for help) > ").strip().lower()

    cmd = app.getCommand(userInput)
    if cmd:
        cmd()
    else:
        print(f"{Color.RED.value}No command found, use 'h' for help.{Color.RESET.value}")
