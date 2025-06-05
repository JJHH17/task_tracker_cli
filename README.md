# task_tracker_cli
A simple task tracker, usable via the CLI.

# Info:
- This tool allows users to Add, Delete, Edit and Get Tasks populated via the command line.
- Project specifications can be found via: https://roadmap.sh/projects/task-tracker

# Project Requirements:
- Python 3 is needed in order for the programto be initially executed.
- The project will generate a "tasks.json" in the projects directory, this contains the relevant Tasks.
- No external libraries or installations are required for this project, although Python libraries are imported.
- The JSON, OS and Pathlib libraries are imported for this project.b

# Running the tool:
1. 'cd' to the project directory once you've cloned the repo.
2. Run ```python3 main.py``` to initiate the project.
3. Follow the commands as fed back via the command line.

- Add = Allows you to add a new Task.
- Description = Allows you to edit the description of an existing Task.
- Status = Allows you to change the status of an existing Task.
- Completed = Allows you to set the status of a given Task to "Done".
- Delete = Allows you to delete a Task.
- Get = Fetches a list of all existing Tasks.
- Get Completed = Fetches a list of all completed tasks.
- Get Uncompleted = Fetches a list of all Tasks that are not completed.
- Get In Progress = Fetches a list of all Tasks that are "In Progress" status.
- Exit - Exit the program loop and terminate the program.

# Project Details:
The project runs in an endless loop until the "Exit" keyword is entered.
The project utilizes a "Task" class containing methods that Add, Fetch, Delete and Modify input.
Data is then appended to a JSON file named "tasks.json" - if the file does not exist, a new one is created as the program is executed.
