from bait.core.entities import BaseEntity
from bait.core.entities import Condominium

class Home(BaseEntity):
    def __init__(self,id, condominium, number, home_type, home_owner, residents=[],):
        super().__init__(id)
        self.condominium = condominium
        self.number = number
        self.home_type = home_type
        self.home_owner = home_owner
        self.residents = residents