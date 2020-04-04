from bait.core.use_cases.base_use_case import BaseUseCase

class ListCondominiumsUseCase(BaseUseCase):
    def __init__(self, repo):
        super().__init__(repo)

    def execute(self, request_object=None):
       response = self.repo.list(request_object)
       return response