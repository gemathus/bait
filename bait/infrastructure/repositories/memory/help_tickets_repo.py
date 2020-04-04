from bait.infrastructure.repositories.memory import BaseMemoryRepo
from bait.core.entities.help_ticket import HelpTicket
import uuid

class HelpTicketsRepo(BaseMemoryRepo):
    def __init__(self, data):
        super().__init__(data)

    def create(self, request_object):
        h = HelpTicket(
            id=uuid.uuid4(),
            title=request_object['title'],
            content=request_object['content'],
            resident=request_object['resident']
        )
        self.data.append(h)
        return h