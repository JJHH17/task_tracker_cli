# File responsible for running project
# Program will loop allow user to modify their list until an exit crtieria is met

from tasks import Task
from programMessage import header, body, footer

active = True

while active:
    user_input = input("What would you like to do? ").lower()

    match user_input:
        case "exit":
            active = False

        case "add":
            print("You will add an item")

        case "get":
            print("You will see all items")