from typing import Optional, Any, NoReturn

from icecream import ic

from structures.LinkedList import LinkedList


class Stack:
    """Стэк на основе связного списка."""

    def __init__(self, init_values: Optional[list] = None) -> NoReturn:
        """
        Инициализация стэка.
        :param init_values: список начальных значений.
        """
        self.__ll = LinkedList()

        if init_values is None:
            init_values = []

        for val in init_values:
            self.__ll.append(val)

        # Будем считать количество элементов
        self.length = len(init_values)

    def push(self, value: Any) -> NoReturn:
        """
        Добавляет элемент в конец стэка.
        :param value: значение.
        """
        self.length += 1
        self.__ll.append(value)

    def pop(self) -> Any:
        """
        Удаляет последний элемент из стека и возвращает его.
        :return: значение последнего элемента.
        """
        last = self.__ll.find_by_index(self.length - 1)
        self.__ll.remove_by_index(self.length - 1)
        self.length -= 1
        return last.value

    def peek(self) -> Any:
        """
        Просмотр последнего элемента без удаления.
        :return: значение последнего элемента.
        """
        return self.__ll.find_by_index(self.length - 1).value

    def __str__(self):
        return str(self.__ll)

    __repr__ = __str__


if __name__ == "__main__":
    s = Stack([1, 2, 3])
    ic(s)
    s.push(4)
    s.push(5)
    ic(s.peek())
    ic(s.pop())
    ic(s)
