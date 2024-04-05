from pytest import fixture
from lemon_tcg.context import Context

CONTEXT = Context.get_instance()

@fixture(scope="function", autouse=True)
def setup_tests():
    CONTEXT.reset_config()

    yield

    CONTEXT.reset_config()