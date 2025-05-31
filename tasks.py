# FIle responsible for creating and modifying task objects

class Tasks:
    def __init__(self, request):
        # request arg confirms what user wants to do (edit, remove, etc...)
        self.__id = None # ID for requests
        self.__description = None
        self.__status = None
        self.__created_at = None
        self.__updated_at = None
        self.request = request

