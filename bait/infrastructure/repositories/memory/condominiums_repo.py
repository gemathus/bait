from bait.infrastructure.repositories.memory import BaseMemoryRepo
from bait.core.entities.condominium import Condominium
import uuid

class CondominiumsRepo(BaseMemoryRepo):
    def __init__(self, data=[]):
        super().__init__(data)
    
    def create(self, request_object):
        request_object['id'] = str(uuid.uuid4())
        c = Condominium.from_dict(request_object)
        self.data.append(c)
        return c
        