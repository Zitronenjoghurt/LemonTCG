from pytest import fixture
from lemon_tcg.entities.card import Card

@fixture
def babu():
    return Card.load_from_id(id="babu")

def test_load_from_id(babu: Card):
    assert isinstance(babu, Card)
    assert babu.id == "babu"