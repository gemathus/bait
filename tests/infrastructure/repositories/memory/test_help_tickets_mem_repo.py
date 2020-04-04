import pytest

from bait.core.entities import HelpTicket
from bait.core.entities import Resident
from bait.core.entities import Condominium
from bait.core.entities import Home
from bait.core.entities import HomeOwner
from bait.core.entities import HomeType

from bait.infrastructure.repositories.memory import HelpTicketsRepo

@pytest.fixture
def resident():
    c = Condominium(1, "Puerta del sol","Privada de la Cañanda 60")
    owner = HomeOwner(1, "Aarón", "Pasol", "aaron@jerusalem.jud")
    home = Home(1, c, "203", HomeType.APPARTMENT, owner)
    return Resident(1, "Gerardo", "Mathus", "gerardo@nextia.mx", home)

@pytest.fixture
def help_tickets(resident):
    return [
        HelpTicket(1, resident, "No hay agua", "No ha habido agua desde hace un chingo"),
        HelpTicket(2, resident, "Se fue la luz", "La luz se fue como a las 7 am y se me apagó la compu."),
        HelpTicket(3, resident, "Pasillo sucio", "Hay algo pegajoso y asqueroso"),
        HelpTicket(4, resident, "Basura", "No pasan a recoger la basura.")
    ]
def test_list_all_help_tickets(help_tickets):
    repo = HelpTicketsRepo(help_tickets)
    request_object={'filters': ""}
    result = repo.list(request_object)
    assert len(result) == len(help_tickets)

def test_list_help_tickets_with_limit_filter(help_tickets):
    repo = HelpTicketsRepo(help_tickets)
    request_object={'filters': "limit=2"}
    result = repo.list(request_object)
    assert len(result) == 2

    request_object = {"filters":"limit=1&offset=0"}
    result = repo.list(request_object)
    assert len(result) == 1
    assert result[0].title == "No hay agua"

    request_object = {"filters": "limit=1&offset=2"}
    result = repo.list(request_object)
    assert len(result) == 1
    assert result[0].title == "Pasillo sucio"

    request_object = {"filters": "limit=2&offset=2"}
    result = repo.list(request_object)
    assert len(result) == 2
    assert result[0].title == "Pasillo sucio"
    assert result[1].title == "Basura"

    request_object = {"filters": "limit=1000&offset=0"}
    result = repo.list(request_object)
    assert len(result) == len(help_tickets)
    assert result[0] == help_tickets[0]
    assert result[3] == help_tickets[3]

    request_object = {"filters": "limit=10&offset=10"}
    result = repo.list(request_object)
    assert len(result) == 0

def test_create_help_ticket(help_tickets, resident):
    request_object = {
        "title":"Gel antibacterial",
        "content":"En las entradas debería haber gel antibacterial por la situación actual. Sin embargo, todos los dispensadores están vacíos.",
        "resident":resident
    }
    repo = HelpTicketsRepo(help_tickets)
    help_ticket = repo.create(request_object)
    assert isinstance(help_ticket, HelpTicket)
    assert help_ticket.title == request_object['title']
    assert len(repo.list()) == 5