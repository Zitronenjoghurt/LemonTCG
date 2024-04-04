from pytest import fixture
from src.constants.language import Language
from src.entities.localized_value import LocalizedValue

@fixture
def full():
    return LocalizedValue(
        en="Cheese",
        de="Käse",
        fr="Fromage"
    )

@fixture
def empty():
    return LocalizedValue()

def test_get_value(full: LocalizedValue, empty: LocalizedValue):
    assert full.get_value(language=Language.GERMAN) == "Käse"
    assert full.get_value("bongo") == "Cheese" # type: ignore
    assert empty.get_value() == "missing_translation"