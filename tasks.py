# FIle responsible for creating and modifying task objects

from datetime import datetime # Used to get "Created at" and "Updated at" values

id = 0 # Used to track ID of tasks
tasks = [] # Used to store tasks


class Task:

    def add_item(self, description, status):
        global id # Ensuring that ID is global
        global tasks # Ensuring tasks list is global

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
                

    def add_status(self, id, status):
        for task in tasks:
            if task["ID"] == id:
                task["Status"] = status
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task ID {id} updated successfully.")
                return 
        
        print(f"Task ID {id} not found.")


    def update_status(self, id, status):
        for task in tasks:
            if task["ID"] == id:
                task["Status"] = status
                task["Updated"] = datetime.today().strftime("%d-%m-%y")
                print(f"Task ID {id} updated successfully")
                return
            
        print(f"Task ID {id} not found.")


    def complete_task(self, id):
        pass # Pass ID to auto complete task


    def delete_task(self, id):
        pass # Pass ID to delete task (require user to validate before deletion)


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


james = Task()
james.add_item("Water plants", "New")
james.add_item("run", "New")
james.get_tasks()
james.update_description(1, "don't water plants")
james.update_description(2, "cry")
james.update_description(100, "Hello world")
james.add_status(10, "Completed")
james.add_status(2, "nearly done")
james.get_tasks()
