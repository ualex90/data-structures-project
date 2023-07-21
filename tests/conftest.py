import pytest

from src.stack import Stack


@pytest.fixture
def stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s
