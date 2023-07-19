"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack


def test_node():
    """Тестирование класса Node."""
    # Test case 1 # Node attribute
    first = Node(1, None)
    second = Node(2, first)
    assert first.data == 1
    assert second.data == 2
    assert first.next_node is None


def test_stack():
    """Тестирование класса Stack."""
    # Test case 1 # Stack.push()
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.top.data == 3
    assert s.top.next_node.data == 2
    assert s.top.next_node.next_node.data == 1
    assert s.top.next_node.next_node.next_node is None

    # Test case 1 # Stack.pop()
    assert s.pop() is None
