class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = "TreeNode(data={}, left={}, right={})"
        return fmt.format(self.data, self.left, self.right)

class BinarySearchTree:
    def __init__(self, tree_data):
        def place(node, data):
            if(node.data < data):
                if(node.right):
                    place(node.right, data)
                else:
                    node.right = TreeNode(data)
            elif(node.data >= data):
                if(node.left):
                    place(node.left, data)
                else:
                    node.left = TreeNode(data)
        head = TreeNode(tree_data.pop(0))
        self._data = head
        for d in tree_data:
            place(head, d)

    def data(self):
        return self._data

    def sorted_data(self, node = None):
        if(not node):
            node = self._data
        if(node.right and node.left):
            return self.sorted_data(node.left) + [node.data] + self.sorted_data(node.right)
        elif(node.right):
            return [node.data] + self.sorted_data(node.right)
        elif(node.left):
            return self.sorted_data(node.left) + [node.data]
        else: 
            return [node.data]