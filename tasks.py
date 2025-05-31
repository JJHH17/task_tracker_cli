# FIle responsible for creating and modifying task objects

from datetime import datetime # Used to get "Created at" and "Updated at" values


class Task:
    def __init__(self, user_name):
        self.name = user_name
        self.task_list = [] # This will store our tasks
        self.ID = 0 # This will increment when tasks are added

        self.__task = {
            "ID": None,
            "Description": None, 
            "Status": None,
            "Created": None,
            "Updated": None,
        } # contains tasks created

        # Updates "Created at" value
        self.__task["Created"] = datetime.today().strftime("%d-%m-%y")

    def add_description(self, description):
        self.ID += 1
        self.__task["ID"] = self.ID
        self.__task["Description"] = description
        self.__task["Updated"] = datetime.today().strftime("%d-%m-%y")
        # Appending to list 
        self.task_list.append(self.__task)
        print(self.task_list)

    def update_description(self, id, description):
        # TODO: Add logic to check ID
        self.__task["Description"] = description
        self.__task["Updated"] = datetime.today().strftime("%d-%m-%y")

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
        pass # Fetch a list of all tasks

    def get_completed(self):
        pass 

    def get_uncompleted(self):
        pass

    def get_inprogress(self):
        pass

    def append_to_list(self):
        pass # Appends to list when method is called

james = Task("james")
james.add_description("Water plants")
james.add_description("Hello")
melissa = Task("Melissa")
melissa.add_description("Test")