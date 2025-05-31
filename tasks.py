# FIle responsible for creating and modifying task objects

tasks = [] # This will store our tasks

class Task:
    def __init__(self, user_name):
        self.name = user_name
        self.task_list = [] # This will store our tasks

        self.__task = {
            "ID": None,
            "Description": None, 
            "Status": None,
            "Created At": None,
            "Updated At": None,
        } # contains tasks created

    def add_description(self, description):
        self.__task["Description"] = description
        # Append to task list

    def update_description(self, description):
        pass

    def add_status(self, status):
        pass

    def update_status(self, status):
        pass

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