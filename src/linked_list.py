from src.node import Node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Инициализация"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is not None:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data, None)
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail is not None:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node
        else:
            self.tail = Node(data, None)
            self.head = self.tail

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке"""
        node = self.head
        ll_list = list()
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, user_id: int) -> dict:
        """
        Возвращает первый найденный в LinkedList словарь с ключом
        'id', значение которого равно переданному в метод значению
        """
        pass

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.lstrip()
