from typing import NoReturn, Any

from icecream import ic


class BinaryTree:
    class Node:
        """Класс узла дерева"""

        def __init__(self, value: Any) -> NoReturn:
            self.value = value
            self.left = self.right = None

        def __str__(self):
            """Преобразование узла к строке"""
            return f"Node({self.value})"

        # И это тоже преобразование к строке
        __repr__ = __str__

    def __init__(self):
        self.root = None

    def add(self, value: Any) -> NoReturn:
        """
        Публичная функция добавления элемента.
        :param value: значение, которое нужно добавить.
        """
        # Если дерево пустое, то добавляем в корень
        if self.root is None:
            self.root = self.Node(value)
        else:
            # Иначе рекурсивно ищем место для вставки
            self._add(self.root, value)

    def _add(self, node: Node, value: Any) -> NoReturn:
        """
        Рекурсивая функция вставки элемента.
        :param node: текущий узел.
        :param value: значение.
        """
        # Если значение меньше, чем в текущем узле, то нужно вставлять в левое поддерево
        if value < node.value:
            # Если левое поддерево пусто, то просто добавляем узел
            if node.left is None:
                node.left = self.Node(value)
            else:
                # Иначе вызываем рекурсию с левым поддеревом
                self._add(node.left, value)
        else:
            # С правым полностью аналогично
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._add(node.right, value)

    def find(self, value: Any) -> Node:
        """
        Публичная функция поиска.
        :param value: значение для поиска.
        :return: узел со значением value.
        """
        # Если дерево пусто, то конец
        if self.root is None:
            raise ValueError("No such value")
        else:
            # Иначе рекурсивный поиск
            return self._find(self.root, value)

    def _find(self, node, value) -> Node:
        """
        Рекурсивный поиск.
        :param node: узел, в котором ищем.
        :param value: искомое значение.
        :return:
        """
        # Если узла не существует, то конец
        if node is None:
            raise ValueError("No such value")
        # Если значения равны, то узел найден
        if value == node.value:
            return node
        # Если меньше, то ищем в левом поддереве
        if value < node.value:
            return self._find(node.left, value)
        # Если больше - в правом
        if value > node.value:
            return self._find(node.right, value)

    def destroy(self):
        """Удаляет корень дерева."""
        self.root = None


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    #     3
    #  0     4
    #    2      8
    ic(tree.find(0))  # ic| tree.find(0): Node(0)
    ic(tree.find(8))  # ic| tree.find(8): Node(8)
    ic(tree.find(12))  # ValueError: No such value
