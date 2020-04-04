from bait.infrastructure.repositories.memory import CondominiumsRepo
from bait.core.use_cases import CreateCondominiumUseCase
from bait.core.use_cases import ListCondominiumsUseCase
condo_repo = CondominiumsRepo()
uc_create_condo = CreateCondominiumUseCase(condo_repo)
uc_list_condos = ListCondominiumsUseCase(condo_repo)
while True:
    print("-----------------------Condominios-----------------------")
    for i,c in enumerate(uc_list_condos.execute(request_object={"filters":""})):
        print("{}: {}".format(i, c))
    print("--------------------------------------------------------")
    name = input("Nombre del condominio: ")
    address= input("Dirección: ")
    uc_create_condo.execute(request_object={"name":name,"address":address})