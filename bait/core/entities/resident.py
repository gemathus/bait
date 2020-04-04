from bait.core.entities import Person
from bait.core.entities import BaseEntity

class Resident(BaseEntity, Person):
    def __init__(self,id,name,last_name, email, home):
        BaseEntity.__init__(self, id)
        Person.__init__(self,name, last_name, email)
        self.home = home