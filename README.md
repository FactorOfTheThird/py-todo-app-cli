# Barebones CLI Todo app built with Python

It's purpose was to quickly get my hands dirty with python as I explore more intricate parts of the language.

## Usage

Simply clone the `main.py` file and run it in a terminal.

The following commands are available:

| Command | Description |
|----------|----------|
| q    | Quits the app, does not save automatically. |
| h    | Displays the list of commands and their description in-terminal. |
| list    | Lists all the tasks currently loaded in the terminal. |
| add | Prompts the user for a title and description of the new task. |
| rem | Removes the task by it's ID |
| load | Loads tasks from a JSON file (needs to be in the same directory). |
| save | Saves all tasks currently in the app to an adjacent JSON file |

## Adding commands and functionality

At the moment, commands are stored in the `App` class:

```py
self.commands = {
    "h": self.help,
    "q": self.quit,

    "add": self.addTask,
    "list": self.listTasks,
    "rem": self.removeTask,

    "save": self.saveTasks,
    "load": self.importTasks
}
```

To add a new command, simply add a new entry in the dictionary where the key is the command and the value is the function that will be executed when running the command.