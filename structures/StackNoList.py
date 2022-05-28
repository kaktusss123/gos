from icecream import ic

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.value})"


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        elif self.head == self.tail:
            tmp = self.tail
            self.tail = self.head = None
            return tmp
        else:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return tmp

    def peek(self):
        return self.tail


if __name__ == '__main__':
    s = Stack()
    ic(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    ic(s.is_empty())
    ic(s.pop())
    ic(s.pop())
    ic(s.pop())
    ic(s.is_empty())
