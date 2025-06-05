# File responsible for running project
# Program will loop allow user to modify their list until an exit criteria is met

from tasks import Task, tasks
from programMessage import header

active = True # Used to loop through program until exit prompt is entered

user = Task() # Intializing an instance

while active:
    user_input = input("""\n_______________________________________________\n
What would you like to do? (Add | Description | Status | Completed | Get | Get Completed | Get Uncompleted | Get In Progress | Exit) : """).lower().strip()

    match user_input:
        # Exit criteria
        case "exit":
            active = False

        case "add":
            # Allows user to add a new task
            description = input("\nWhat would you like to add? ")
            add_flag = True

            while add_flag:
                status = input("\nPlease enter the status of this item (To Do | In Progress | Done): ").title().strip()
                match status:
                    case "To Do" | "In Progress" | "Done":
                        user.add_item(description, status)
                        add_flag = False

                    case _:
                        print("\nInvalid status, please enter")

        case "description":
            # Allows user to change description of given task
            id = int(input("\nPlease enter a Task ID: "))
            description = input("\nPlease enter a description: ")

            user.update_description(id, description)

        case "status":
            # Allows user to change status of given task
            id = int(input("\nPlease enter a Task ID: "))
            status_flag = True

            while status_flag:
                status = input("\nPlease enter the status of this item (To Do | In Progress | Done): ")
                match status:
                    case "to do" | "in progress" | "done":
                        user.update_status(id, status)
                        status_flag = False

                    case _:
                        print("\nInvalid status, please enter")

        case "completed":
            # Auto completes a given task
            id = int(input("\nPlease enter a Task ID: "))
            user.complete_task(id)

        case "delete":
            # Deletes a given entry
            id = int(input("\nPlease enter the ID of the task you wish to delete: "))
            user.delete_task(id)

        case "get":
            # Fetches a list of all tasks
            user.get_tasks()

        case "get completed":
            # Fetches a list of all completed tasks
            user.get_completed()

        case "get uncompleted":
            # Fetches a list of all uncompleted tasks
            user.get_uncompleted()

        case "get in progress":
            # Fetches a list of all in progress tasks
            user.get_inprogress()
