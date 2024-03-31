import pytest


@pytest.fixture()
def set_up():
    print("Start")
    yield
    print("Finish")

@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")
