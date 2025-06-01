# File responsible for running project
# Program will loop allow user to modify their list until an exit criteria is met

from tasks import Task, tasks
from programMessage import header, body, footer

active = True

user = Task() # Intializing an instance

while active:
    user_input = input("What would you like to do? ").lower()

    match user_input:
        case "exit":
            active = False

        case "add":
            description = input("What would you like to add? ")
            add_flag = True

            while add_flag:
                status = input("Please enter the status of this item (ToDo | In Progress | Done): ").lower()
                match status:
                    case "todo" | "in progress" | "done":
                        user.add_item(description, status)
                        add_flag = False

                    case _:
                        print("Invalid status, please enter")

        case "description":
            id = input("Please enter a Task ID: ")
            description = input("Please enter a description: ")

            user.update_description(id, description)

        case "get":
            for task in tasks:
                print(task)