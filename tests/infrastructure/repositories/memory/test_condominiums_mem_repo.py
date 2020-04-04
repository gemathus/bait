import pytest

from bait.core.entities import Condominium
from bait.infrastructure.repositories.memory.condominiums_repo import CondominiumsRepo

@pytest.fixture
def condominiums():
    return [
        Condominium(1, "Puerta del Sol", "Privada de la Cañada 60, Bosque Real"),
        Condominium(2, "Latitud Polanco", "Av. Ejército Nacional 453, Granada"),
        Condominium(3, "Arquímedes 95", "Arquimedes 95 Colonia Polanco")
    ]

def test_list_condominius(condominiums):
    repo = CondominiumsRepo(condominiums)
    
    assert len(repo.list()) == len(condominiums)
    
    request_object = {"filters":"limit=1&offset=0"}
    assert len(repo.list(request_object)) == 1

def test_create_condominium(condominiums):
    repo = CondominiumsRepo(condominiums)
    request_object = {"name":"Miyana", "address": "Miguel de Cervantes Saavedra 198"}
    condo = repo.create(request_object)
    assert isinstance(condo, Condominium)
    assert len(repo.list()) == 4
    assert repo.list()[-1] == condo