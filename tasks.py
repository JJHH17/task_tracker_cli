# FIle responsible for creating and modifying task objects

from datetime import datetime # Used to get "Created at" and "Updated at" values

id = 0 # Used to track ID of tasks
tasks = [] # Used to store tasks


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
        self.__task["Description"] = description
        self.__task["Status"] = status
        self.__task["Updated"] = datetime.today().strftime("%d-%m-%y")

        tasks.append(self.__task) # Appending to list to contain tasks


    def update_description(self, id, description):
        for task in tasks:
            if task["ID"] == id:
                task["Description"] = description
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task {id} updated successfully.")
                return # Prevents belowrejection message from being looped
            
        print(f"Task ID {id} not found.")


    def update_status(self, id, status):
        for task in tasks:
            if task["ID"] == id:
                task["Status"] = status
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task ID {id} updated successfully.")
                return
            
        print(f"Task ID {id} not found.")


    def complete_task(self, id):
        for task in tasks:
            if task["ID"] == id:
                task["Status"] = "Done"
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task ID {id} completed!")
                return
            
        print(f"Task ID {id} not found.")


    def delete_task(self, id):
        # TODO: Pass in ID, delete given entry if found, error if not, then change ID's to move down
        found_id = False # Flag used to track each item

        for i, task in enumerate(tasks):
            if task["ID"] == id:
                found_id = True
                del tasks[i] # We remove via index
                break

        if not found_id:
            print(f"Task ID {id} not found.")
            return

        # Looping across remaining tasks to change their ID
        for i, task in enumerate(tasks):
            task["ID"] = i + 1 # Starting from 1, as this is ID starting point

        print(f"Task ID {id} removed successfully.")


    def get_tasks(self):
        # Fetch a list of all tasks
        for item in tasks:
            print(item)


    def get_completed(self):
        pass 


    def get_uncompleted(self):
        pass


    def get_inprogress(self):
        pass


    def append_to_list(self):
        pass # Appends to list when method is called

