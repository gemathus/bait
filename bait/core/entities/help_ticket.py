from bait.core.entities import BaseEntity
class HelpTicket(BaseEntity):
    def __init__(self,id=None,resident=None, title=None,content=None):
        super().__init__(id)
        self.resident = resident
        self.title = title
        self.content = content
        self.attachments = []
    def __str__(self):
        return "({}) {}: {}".format(self.resident.full_name(), self.title, self.content)