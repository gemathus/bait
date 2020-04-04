from bait.core.use_cases import BaseUseCase
class ListHelpTicketsUseCase(BaseUseCase):
    def __init__(self, repo):
        super().__init__(repo)

    def execute(self,request_object = None):
        return self.repo.list(request_object)