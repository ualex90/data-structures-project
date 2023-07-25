import pytest

from src.queue import Queue
from src.stack import Stack


@pytest.fixture
def stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s


@pytest.fixture
def queue():
    q = Queue()
    q.enqueue('data1')
    q.enqueue('data2')
    q.enqueue('data3')
    return q
