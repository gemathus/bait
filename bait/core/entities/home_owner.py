from bait.core.entities import BaseEntity
from bait.core.entities import Person

class HomeOwner(BaseEntity, Person):
    def __init__(self, id, name, last_name, email, homes = []):
        BaseEntity.__init__(self, id)
        Person.__init__(self, name, last_name, email)
        self.homes = homes