from typing import Any, NoReturn, Optional
from icecream import ic  # pip install icecream


class LinkedList:
    class Node:
        def __init__(self, value: Any) -> NoReturn:
            """
            Создает узел с заданным значением.
            :param value: значение.
            """
            self.value = value
            self.next = None

        def __str__(self):
            return f"Node({self.value})"

        __repr__ = __str__

    def __init__(self) -> NoReturn:
        """Инициализирует пустой связный список."""
        self.head = None

    def append(self, value: Any) -> NoReturn:
        """
        Добавляет узел в конец.
        :param value: значение узла.
        """
        # Если список пуст, то сразу ставим в head
        if self.head is None:
            self.head = self.Node(value)
        else:
            # Если не пуст, то идем до конца списка
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            # В конце вставляем
            cur.next = self.Node(value)

    def find_by_value(self, value: Any) -> Optional[Any]:
        """
        Находит узел по значению.
        :param value: значение.
        """
        cur = self.head
        # Пока не упремся в конец
        while cur is not None:
            # сравниваем значения
            if cur.value == value:
                return cur
            cur = cur.next
        else:
            # Это если дошли до конца и не нашли
            raise ValueError(f"No such value: {value}")

    def find_by_index(self, index: int) -> Optional[Any]:
        """
        Находит узел по индексу.
        :param index: искомый индекс.
        """
        cur = self.head
        # Получаем cur.next столько раз, сколько нужно по индексу
        for i in range(index):
            if cur is None:
                # Если элементов не хватает, то исключение
                raise IndexError(f"No such index: {index}")
            cur = cur.next
        return cur

    def remove_by_index(self, index: int) -> NoReturn:
        """
        Удаляет по индексу.
        :param index: индекс.
        """
        # Ищем предыдущий
        cur = self.find_by_index(index - 1)
        # Пропускаем удаляемый элемент
        cur.next = cur.next.next

    def __str__(self):
        lst = []
        cur = self.head
        while cur is not None:
            lst.append(cur.value)
            cur = cur.next
        return str(lst)

    __repr__ = __str__


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ic(ll)                   # ic| ll: [1, 2, 3, 4, 5]
    ic(ll.find_by_index(2))  # ic| ll.find_by_index(2): Node(3)
    ic(ll.find_by_value(3))  # ic| ll.find_by_value(3): Node(3)
    ll.remove_by_index(2)
    ic(ll)                   # ic| ll: [1, 2, 4, 5]
    # ll.find_by_index(11)   # IndexError: No such index: 11
    # ll.find_by_value(11)   # ValueError: No such value: 11
    # ll.remove_by_index(11) # IndexError: No such index: 10
