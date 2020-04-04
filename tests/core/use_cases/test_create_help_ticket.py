import pytest
from unittest import mock
from datetime import datetime

from bait.core.entities import HelpTicket
from bait.core.entities import Resident
from bait.core.entities import Condominium
from bait.core.entities import Home
from bait.core.entities import HomeOwner
from bait.core.entities import HomeType

from bait.core.use_cases import CreateHelpTicketUsecase
from bait.core.use_cases import ListHelpTicketsUseCase

@pytest.fixture
def resident():
    c = Condominium(1, "Puerta del sol","Privada de la Cañanda 60")
    owner = HomeOwner(1, "Aarón", "Pasol", "aaron@jerusalem.jud")
    home = Home(1, c, "203", HomeType.APPARTMENT, owner)
    return Resident(1, "Gerardo", "Mathus", "gerardo@nextia.mx", home)

@pytest.fixture
def tickets(resident):
    return [
        HelpTicket(1, resident, "No hay agua", "No ha habido agua desde hace un chingo"),
        HelpTicket(2, resident, "Se fue la luz", "La luz se fue como a las 7 am y se me apagó la compu."),
        HelpTicket(3, resident, "Pasillo sucio", "Hay algo pegajoso y asqueroso"),
        HelpTicket(4, resident, "Basura", "No pasan a recoger la basura.")
    ]

def test_save_help_ticket(resident):
    req_obj = {
        "id":1,
        "resident": resident,
        "title":"No hay agua",
        "content":"No ha habido agua desde hace un chingo"
    }
    help_ticket = HelpTicket(1, resident, "No hay agua", "No ha habido agua desde hace un chingo")

    repo = mock.Mock()
    repo.create.return_value = help_ticket
    create_ticket = CreateHelpTicketUsecase(repo)
    result = create_ticket.execute(req_obj)

    assert result.resident == resident
    assert result.title == "No hay agua"

def test_list_help_tickets(tickets):
    repo = mock.Mock()
    repo.list.return_value = tickets
    list_tickets = ListHelpTicketsUseCase(repo)
    result = list_tickets.execute()
    repo.list.assert_called_with(None)
    assert result == tickets
    assert result[2].title == "Pasillo sucio"
