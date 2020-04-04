from bait.core.use_cases.base_use_case import BaseUseCase

class CreateCondominiumUseCase(BaseUseCase):
    def __init__(self, repo):
        super().__init__(repo)

    def execute(self, request_object):
       new_condo = self.repo.create(request_object)
       return new_condo