"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList


def test_linkedlist(ll_1, ll_2):
    # Test case #1
    assert str(ll_1) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
    assert str(ll_2) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> None"
    # Test case #2
    assert ll_1.head.data == {'id': 0}
    assert ll_1.head.next_node.data == {'id': 1}
    assert ll_1.tail.next_node is None
    # Test case #3
    ll_3 = LinkedList()
    assert str(ll_3) == "None"


def test_to_list(ll_1, ll_3):
    # Test case #1
    assert ll_1.to_list() == [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}]
    assert ll_3.to_list() == []


def test_get_data_by_id(ll_1, ll_3):
    assert ll_1.get_data_by_id(2) == {'id': 2}
    assert ll_1.get_data_by_id(3) == {'id': 3}
    assert ll_1.get_data_by_id(4) is None
    ll_1.insert_at_end('idusername')
    ll_1.insert_at_end([1, 2, 3])
    assert ll_1.get_data_by_id(4) is None
    assert ll_3.get_data_by_id(1) is None
