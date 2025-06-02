# File responsible for running project
# Program will loop allow user to modify their list until an exit criteria is met

from tasks import Task, tasks
from programMessage import header, body, footer

active = True

user = Task() # Intializing an instance

while active:
    user_input = input("What would you like to do? ").lower()

    match user_input:
        # Exit criteria
        case "exit":
            active = False

        case "add":
            # Allows user to add a new task
            description = input("What would you like to add? ")
            add_flag = True

            while add_flag:
                status = input("Please enter the status of this item (To Do | In Progress | Done): ").lower()
                match status:
                    case "to do" | "in progress" | "done":
                        user.add_item(description, status)
                        add_flag = False

                    case _:
                        print("Invalid status, please enter")

        case "description":
            # Allows user to change description of given task
            id = int(input("Please enter a Task ID: "))
            description = input("Please enter a description: ")

            user.update_description(id, description)

        case "status":
            # Allows user to change status of given task
            id = int(input("Please enter a Task ID: "))
            status_flag = True

            while status_flag:
                status = input("Please enter the status of this item (To Do | In Progress | Done): ").lower()
                match status:
                    case "to do" | "in progress" | "done":
                        user.update_status(id, status)
                        status_flag = False

                    case _:
                        print("Invalid status, please enter")

        case "complete":
            # Auto completes a given task
            id = int(input("Please enter a Task ID: "))
            user.complete_task(id)

        case "delete":
            # Deletes a given entry
            id = int(input("Please enter the ID of the task you wish to delete: "))
            user.delete_task(id)

        case "get":
            # Fetches a list of all tasks
            for task in tasks:
                print(task)