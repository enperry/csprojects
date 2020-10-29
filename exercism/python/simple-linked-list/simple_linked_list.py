class Node:
    def __init__(self, value):
        self.val = value
        self.n = None

    def value(self):
        return self.val

    def next(self):
        return self.n


class LinkedList:
    def __init__(self, values = []):
        self.h = None
        for value in values:
            self.push(value)

    def __len__(self):
        length = 0
        node = self.h
        while node:
            length = length + 1
            node = node.next()
        return length

    def __iter__(self):
        values = []
        node = self.h
        while node:
            values.append(node.val)
            node = node.next()
        return iter(values)

    def head(self):
        if self.h is None:
            raise EmptyListException("empty list")

        return self.h

    def push(self, value):
        node = Node(value)
        node.n = self.h
        self.h = node

    def pop(self):
        result = self.head().val
        self.h = self.h.n
        return result

    def reversed(self):
        result = LinkedList()
        node = self.h
        while node:
            result.push(node.val)
            node = node.next()
        return result


class EmptyListException(Exception):
    pass