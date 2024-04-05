from pytest import fixture
from lemon_tcg.constants.language import Language
from lemon_tcg.entities.config import Config

@fixture
def config():
    return Config()

def test_set_language(config: Config):
    assert config.language == Language.ENGLISH
    config.set_language(language=Language.GERMAN)
    assert config.language == Language.GERMAN
    config.set_language(language=Language.FRENCH)
    assert config.language == Language.FRENCH

def test_save_state(config: Config):
    config.set_language(language=Language.GERMAN)
    config.save_state()

    new_config = Config.load_state()
    assert new_config.language == Language.GERMAN