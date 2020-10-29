class Node:
    # why are they named like this. exercism why
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head.prev = self.head
    
    def link(self, value, prev):
        node = Node(value, prev.next, prev)
        node.prev.next = node
        node.next.prev = node

    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.value
    
    def shift(self):
        return self.unlink(self.head.next)

    def unshift(self, value):
        self.link(value, self.head)

    def pop(self):
        return self.unlink(self.head.prev)

    def push(self, value):
        self.link(value, self.head.prev)