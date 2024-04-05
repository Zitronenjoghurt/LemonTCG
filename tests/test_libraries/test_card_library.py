from lemon_tcg.entities.card import Card
from lemon_tcg.libraries.card_library import CardLibrary

CL = CardLibrary.get_instance()

def test_get_by_id():
    babu = CL.get_by_id(id="babu")
    assert isinstance(babu, Card)
    assert babu.id == "babu"