class Zipper:
    def __init__(self, tree = None, parent = None):
        self.tree = tree
        self.parent = parent

    def __repr__(self):
        return f"{self.tree}"

    def update(self, side, child):
        self.tree[side] = child

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        if(self.tree):
            return self.tree["value"]
        return None

    def set_value(self, value):
        tree = self.tree
        tree["value"] = value
        return Zipper(tree, self.parent)

    def left(self):
        if(not self.tree["left"]):
            return None
        return Zipper(self.tree["left"], self)

    def set_left(self, left):
        tree = self.tree
        tree["left"] = left
        return Zipper(tree, self.parent)

    def right(self):
        if(not self.tree["right"]):
            return None
        return Zipper(self.tree["right"], self)

    def set_right(self, right):
        tree = self.tree
        tree["right"] = right
        return Zipper(tree, self.parent)

    def up(self):
        if(self.parent is None):
            return None
        return Zipper(self.parent.tree, self.parent.parent)

    def to_tree(self):
        root = self
        while(root.parent):
            root = root.parent
        return root.tree