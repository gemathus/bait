from datetime import datetime
class BaseEntity:
    def __init__(self,id):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return "{}".format(self.__dict__)