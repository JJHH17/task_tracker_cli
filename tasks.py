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
            if id in task.values():
                task["Description"] = description
                task["Updated"] = datetime.today().strftime("%d-%m-%y")


    def add_status(self, id, status):
        # TODO: Add logic to check ID
        # TODO: Only allow user to append "NEW, ONGOING, COMPLETED" as status
        # TODO: APPEND TO LIST
        self.__task["Status"] = status
        self.__task["Updated"] = datetime.today().strftime("%d-%m-%y")


    def update_status(self, status):
        # TODO: Add logic to check ID
        # TODO: error if ID doesn't exist
        self.__task["Status"] = status
        self.__task["Updated"] = datetime.today().strftime("%d-%m-%y")


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
james.get_tasks()