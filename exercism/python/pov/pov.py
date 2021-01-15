from json import dumps

class Tree:
    def __init__(self, label, children = None):
        self.label = label
        self.children = children
        if(self.children is None):
            self.children = []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent = None):
        return dumps(self.__dict__(), indent = indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return other is not None and self.__dict__() == other.__dict__()

    def contains_node(self, node):
        if(self.label == node):
            return True
        else:
            return any([c.contains_node(node) for c in self.children])

    def from_pov(self, from_node, skip = None):
        if(from_node == self.label):
            return self
        for c in self.children:
            if(skip != c and c.contains_node(from_node)):
                self.children.remove(c)
                c.children.append(self)
                res = c.from_pov(from_node, skip = self)
                return res
        raise ValueError(f"Target {from_node} does not exist.")

    def path_to(self, from_node, to_node):
        def construct_path_to_node(tree):
            if(tree.label == to_node):
                return [tree.label]
            for c in tree.children:
                if(c.contains_node(to_node)):
                    return [tree.label] + construct_path_to_node(c)
            raise ValueError(f"Target {to_node} does not exist.")
        t = self.from_pov(from_node)
        return construct_path_to_node(t)