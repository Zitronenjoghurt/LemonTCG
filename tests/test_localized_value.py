from pytest import fixture
from lemon_tcg.constants.language import Language
from lemon_tcg.entities.localized_value import LocalizedValue

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