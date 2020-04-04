from bait.core.entities import BaseEntity
class Condominium(BaseEntity):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address
        self.slug = name.lower().replace(" ", "-")

    def __str__(self):
        return "{}: {}".format(self.name, self.address)

    @classmethod
    def from_dict(cls, dict):
        return cls(
            id=dict['id'],
            name=dict['name'],
            address=dict['address']
        )
    