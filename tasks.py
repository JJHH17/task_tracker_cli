# FIle responsible for creating and modifying task objects

from datetime import datetime # Used to get "Created at" and "Updated at" values
from fileHandler import append_file, feed_file, read_file

id = 0 # Used to track ID of tasks
tasks = feed_file() # Used to store tasks

if tasks:
    id = max(task["ID"] for task in tasks)

class Task:

    def add_item(self, description, status):
        global id  # Ensuring that ID is global
        global tasks  # Ensuring tasks list is global
        id += 1
        self.__task = {
            "ID": id,
            "Description": None,
            "Status": None,
            "Created": None,
            "Updated": None,
        } # contains tasks created

        # Updates "Created at" value
        self.__task["Created"] = datetime.today().strftime("%d-%m-%y")
        self.__task["ID"] = id
        self.__task["Description"] = description.capitalize()
        self.__task["Status"] = status.title()
        self.__task["Updated"] = datetime.today().strftime("%d-%m-%y")

        tasks.append(self.__task) # Appending to list to contain tasks
        append_file(tasks) # Appends entry to JSON file


    def update_description(self, id, description):
        for task in tasks:
            if task["ID"] == id:
                task["Description"] = description
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task {id} updated successfully.")

                append_file(tasks)  # Appends entry to JSON file
                return # Prevents below rejection message from being looped
            
        print(f"Task ID {id} not found.")


    def update_status(self, id, status):
        for task in tasks:
            if task["ID"] == id:
                task["Status"] = status.title()
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task ID {id} updated successfully.")
                return
            
        print(f"Task ID {id} not found.")


    def complete_task(self, id):
        # Sets given task ID to Completed status
        for task in tasks:
            if task["ID"] == id:
                task["Status"] = "Done"
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task ID {id} completed!")

                append_file(tasks)  # Appends entry to JSON file
                return
            
        print(f"Task ID {id} not found.")


    def delete_task(self, task_id):
        #  Deletes a task based on given ID
        global id # Passing ID as global for tracking
        found_id = False # Flag used to track each item

        for i, task in enumerate(tasks):
            if task["ID"] == task_id:
                found_id = True
                del tasks[i] # We remove via index
                id = len(tasks) # Changing ID variable to current index length
                break

        if not found_id:
            print(f"Task ID {task_id} not found.")
            return

        # Looping across remaining tasks to change their ID
        for i, task in enumerate(tasks):
            task["ID"] = i + 1 # Starting from 1, as this is ID starting point
            append_file(tasks)  # Appends entry to JSON file

        print(f"Task ID {task_id} removed successfully.")

        # TODO: Ensure program deletes entries via JSON


    def get_tasks(self):
        # Fetch a list of all tasks
        for item in tasks:
            print(item)


    def get_completed(self):
        # Fetches a list of completed items
        completed_tasks = [task for task in tasks if task["Status"] == "Done"]

        if not completed_tasks:
            print("There are currently 0 completed tasks.")
        else:
            for task in completed_tasks:
                print(task)


    def get_uncompleted(self):
        # Fetches a list of uncompleted tasks
        uncompleted_tasks = [task for task in tasks if task["Status"] != "Done"]

        if not uncompleted_tasks:
            print("There are currently 0 uncompleted tasks.")
        else:
            for task in uncompleted_tasks:
                print(task)


    def get_inprogress(self):
        # Fetches a list of in progress tasks
        in_progress = [task for task in tasks if task["Status"] == "In Progress"]

        if not in_progress:
            print("There are currently 0 tasks in progress")
        else:
            for task in in_progress:
                print(task)
