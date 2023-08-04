"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList


def test_linkedlist(ll_1, ll_2):
    assert str(ll_1) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
    assert str(ll_2) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> None"
    ll_3 = LinkedList()
    assert str(ll_3) == "None"
    